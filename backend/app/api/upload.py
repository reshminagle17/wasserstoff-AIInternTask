from fastapi import APIRouter, File, UploadFile
from app.services.document_service  import save_document, extract_text_from_document
import os

router = APIRouter()

@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    try:
        
        folder_path = "backend/data"
        os.makedirs(folder_path, exist_ok=True)

  
        valid_extensions = [".pdf", ".png", ".jpg", ".jpeg"]
        ext = os.path.splitext(file.filename)[1].lower()
        if ext not in valid_extensions:
            return {"error": f"Unsupported file type '{ext}'. Please upload PDF or image file."}

        
        file_location = os.path.join(folder_path, file.filename)
        with open(file_location, "wb") as f:
            content = await file.read()
            f.write(content)

      
        extracted_text = await extract_text_from_document(file_location)

        if not extracted_text.strip():
            return {"error": "File uploaded but no text could be extracted."}

        await save_document(file_location, extracted_text)

        return {
            "message": " Document uploaded and processed successfully!",
            "filename": file.filename,
            "file_path": file_location,
            "extracted_text_snippet": extracted_text[:300] + "..." if len(extracted_text) > 300 else extracted_text
        }

    except Exception as e:
        return {
            "error": str(e),
            "message": "An error occurred while processing the document."
        }




