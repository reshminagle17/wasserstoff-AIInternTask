
from typing import List
import os
from backend.app.services.ocr_utils import extract_text_from_pdf, extract_text_from_image


# Function to extract text from any document (PDF/Image)
async def extract_text_from_document(file_path: str) -> str:
    try:
        if file_path.endswith(".pdf"):
            return extract_text_from_pdf(file_path)
        elif file_path.endswith((".png", ".jpg", ".jpeg")):
            return extract_text_from_image(file_path)
        else:
            return ""
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return ""


# Save extracted text (placeholder for DB/file saving)
async def save_document(file_path: str, extracted_text: str):
    print(f"Saving document: {file_path} with extracted text.")


# (Optional) Get answer logic — not currently used
async def get_answer_from_documents(query: str, documents: List[str]):
    answers = []
    for doc in documents:
        text = await extract_text_from_document(doc)
        if query.lower() in text.lower():
            answers.append(f"Answer from {doc}: {text[:200]}...")  # First 200 characters
    return answers


# Main query search logic
async def search_documents(query: str) -> List[str]:
    folder_path = "backend/data"  # Folder where uploaded files are saved
    matched_docs = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path):
            continue

        text = await extract_text_from_document(file_path)
        print(f"\n--- Extracted text from {filename} ---\n{text[:500]}\n-----------------------------\n")


        if query.lower() in text.lower():
            matched_docs.append(f"{filename} => contains query")

    return matched_docs if matched_docs else ["No documents matched your query."]
