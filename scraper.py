import os
import json
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
from tqdm import tqdm
from datetime import datetime

# Function to parse PDF metadata dates into a readable format (DD/MM/YYYY HH:MM:SS)
def parse_pdf_date_ddmmyyyy(pdf_date):
    try:
        if isinstance(pdf_date, str) and pdf_date.startswith("D:"):
            date_str = pdf_date[2:16]  # Extract YYYYMMDDHHMMSS from metadata
            dt = datetime.strptime(date_str, "%Y%m%d%H%M%S")
            return dt.strftime("%d/%m/%Y %H:%M:%S")
    except:
        return pdf_date  # Return original if parsing fails
    return pdf_date

# CONFIGURATION SETTINGS
BASE_URL = 'https://www.drishtiias.com/hindi/free-downloads/monthly-current-affiars-downloads'
DOWNLOAD_FOLDER = 'downloaded_pdfs'  # Folder to save downloaded PDFs
OUTPUT_JSON = 'pdf_metadata.json'  # JSON file to store metadata

# Create download folder if it doesn't exist
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Fetch the webpage content
response = requests.get(BASE_URL)
soup = BeautifulSoup(response.text, 'html.parser')

# List of years to search for PDF links
years = [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018]

pdf_links = []

# Extract PDF links for each year
for year in years:
    menulist = soup.find(id=f'{year}')  # Find the section for the year
    links_div = soup.find_all(id=f'{year}_child_div')  # Find child div containing links
    for div in links_div:
        links_grp = div.find_all('li', class_='non-list')  # Find list items with links
        for li in links_grp:
            link = li.find('a', href=True)  # Extract the actual link
            pdf_links.append(link['href'])

# List to store metadata of downloaded PDFs
pdf_data_list = []

# Download PDFs and extract metadata with a progress bar
for link in tqdm(pdf_links[1:2], desc="📥 Downloading & Extracting PDFs", unit="pdf"):
    try:
        filename = link.split('/')[-1]  # Extract filename from URL
        file_path = os.path.join(DOWNLOAD_FOLDER, filename)  # Define local save path

        # Download and save the PDF file
        pdf_response = requests.get(link, stream=True)
        with open(file_path, 'wb') as pdf_file:
            for chunk in pdf_response.iter_content(chunk_size=1024):
                pdf_file.write(chunk)

        # Initialize metadata entry
        metadata_entry = {
            'pdf_url': link,
            'local_path': file_path
        }

        try:
            # Read the PDF metadata
            reader = PdfReader(file_path)
            pdf_metadata = reader.metadata
            
            # Extract and clean metadata fields
            for k, v in pdf_metadata.items():
                clean_key = k.lstrip('/')  # Remove leading slash from keys
                value = str(v)  # Convert value to string
                
                # Format date fields properly
                if clean_key in ['CreationDate', 'ModDate']:
                    metadata_entry[clean_key] = parse_pdf_date_ddmmyyyy(value)
                else:
                    metadata_entry[clean_key] = value

        except Exception as e:
            metadata_entry['MetadataError'] = f"Failed to extract metadata: {str(e)}"

        # Add metadata entry to the list
        pdf_data_list.append(metadata_entry)

    except Exception as e:
        print(f"\n[✗] Failed to process {link}: {str(e)}")

# Save all extracted metadata to a JSON file
with open(OUTPUT_JSON, 'w', encoding='utf-8') as json_file:
    json.dump(pdf_data_list, json_file, indent=4)

print(f"\n✅ All metadata saved to {OUTPUT_JSON}")