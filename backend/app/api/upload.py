from fastapi import APIRouter, File, UploadFile
from backend.app.services.document_service import save_document, extract_text_from_document

router = APIRouter()

@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    try:
        file_location = f"documents/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())
        
        # Extract text from the uploaded file (PDF/image)
        extracted_text = await extract_text_from_document(file_location)
        
        # Save the document and its extracted text to the database
        await save_document(file_location, extracted_text)
        
        return {"message": "Document uploaded and processed successfully!"}
    
    except Exception as e:
        return {"error": str(e)}

