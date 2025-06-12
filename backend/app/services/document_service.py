from typing import List, Dict
import os
import pdfplumber
from app.services.ocr_utils import extract_text_from_pdf, extract_text_from_image


# Function to extract text from any document (PDF/Image)
import pdfplumber

async def extract_text_from_document(file_path: str) -> str:
    text = ""
    try:
        if file_path.endswith(".pdf"):
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    print("Extracted:", page_text)  # 👈 ADD THIS
                    if page_text:
                        text += page_text + "\n"

        # fallback to OCR if no text
        if not text.strip():
            print("No text found with pdfplumber. Trying OCR...")
            from .ocr_utils import extract_text_from_image
            text = await extract_text_from_image(file_path)

        return text

    except Exception as e:
        print("Extraction Error:", str(e))
        return ""


# Save extracted text (placeholder for DB/file saving)
async def save_document(file_path: str, extracted_text: str):
    print(f"Saving document: {file_path} with extracted text.")

# Main query search logic with page-paragraph citations
async def search_documents(query: str) -> List[Dict]:
    folder_path = "backend/data"
    matches = []
    query_keywords = query.lower().split()

    for filename in os.listdir(folder_path):
        if not filename.endswith((".pdf", ".png", ".jpg", ".jpeg")):
            continue

        file_path = os.path.join(folder_path, filename)
        if not os.path.isfile(file_path):
            continue

        # --- For PDF files ---
        if filename.endswith(".pdf"):
            try:
                with pdfplumber.open(file_path) as pdf:
                    for i, page in enumerate(pdf.pages, start=1):
                        text = page.extract_text() or ""
                        for para in text.split("\n\n"):
                            if all(word in para.lower() for word in query_keywords):
                                matches.append({
                                    "doc": filename,
                                    "page": i,
                                    "snippet": para.strip()[:200]
                                })
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")
                continue

        # --- For images ---
        else:
            text = extract_text_from_image(file_path)
            if all(word in text.lower() for word in query_keywords):
                matches.append({
                    "doc": filename,
                    "page": None,
                    "snippet": text.strip()[:200]
                })

    return matches if matches else [{"result": "No documents matched your query."}]

