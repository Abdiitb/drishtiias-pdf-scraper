# 📄 DrishtiIAS Monthly Current Affairs PDF Scraper  

This project scrapes and downloads monthly current affairs PDFs from [DrishtiIAS](https://www.drishtiias.com/hindi/free-downloads/monthly-current-affiars-downloads), extracts metadata, and saves it in a JSON file for easy access.  

## ✨ Features  
- 📥 **Automated PDF Downloading**: Fetches PDFs for selected years.  
- 🔍 **Metadata Extraction**: Retrieves metadata such as title, author, creation date, and modification date.  
- 📊 **Structured Output**: Saves extracted metadata in `pdf_metadata.json`.  
- 🚀 **Progress Bar**: Displays real-time download progress using `tqdm`.  

## 🛠 Installation  

Clone the repository:  
```bash
git clone https://github.com/yourusername/drishtiias-pdf-scraper.git
cd drishtiias-pdf-scraper
```

Install dependencies:  
```bash
pip install -r requirements.txt
```

## 🚀 Usage  

Run the script to download PDFs and extract metadata:  
```bash
python scraper.py
```

## 📂 Output Explanation  

After running the script, you will get:  

### 1️⃣ **Downloaded PDFs**  
All downloaded PDFs will be stored inside the `downloaded_pdfs/` folder.  

```
drishtiias-pdf-scraper/
│── downloaded_pdfs/
│   ├── Current_Affairs_January_2024.pdf
│   ├── Current_Affairs_February_2024.pdf
│   └── ...
```

### 2️⃣ **Metadata JSON File (`pdf_metadata.json`)**  
A JSON file named `pdf_metadata.json` will be created in the root directory, containing metadata for each downloaded PDF.  

#### Example JSON Output:  
```json
[
  {
    "pdf_url": "https://www.drishtiias.com/path-to-pdf",
    "local_path": "downloaded_pdfs/Current_Affairs_January_2024.pdf",
    "Title": "Current Affairs January 2024",
    "Author": "DrishtiIAS",
    "CreationDate": "01/01/2024 10:30:00",
    "ModDate": "02/01/2024 12:15:00"
  },
  {
    "pdf_url": "https://www.drishtiias.com/path-to-another-pdf",
    "local_path": "downloaded_pdfs/Current_Affairs_February_2024.pdf",
    "Title": "Current Affairs February 2024",
    "Author": "DrishtiIAS",
    "CreationDate": "01/02/2024 09:45:00",
    "ModDate": "02/02/2024 11:20:00"
  }
]
```

## 🛠 How It Works  

1️⃣ **Scrapes the webpage** for PDF links of the selected years.  
2️⃣ **Downloads PDFs** and stores them in `downloaded_pdfs/`.  
3️⃣ **Extracts metadata** (title, author, creation date, etc.) using `PyPDF2`.  
4️⃣ **Saves metadata** in `pdf_metadata.json`. 
