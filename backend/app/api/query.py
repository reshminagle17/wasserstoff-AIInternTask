# backend/app/api/query.py

from fastapi import APIRouter , Query
from typing import List
from backend.app.services.document_service import search_documents
  # Yeh service ko import kar rahe hain

router = APIRouter()

@router.get("/query/")
async def query_documents(query: str):
    try:
        # Query ke basis pe document search kar rahe hain
        results = await search_documents(query)
        
        if not results:
            return {"message": "No relevant documents found."}
        
        return {"results": results}
    
    except Exception as e:
        return {"error": str(e)}
