from fastapi import APIRouter, Query
from typing import List
from backend.app.services.document_service import search_documents

router = APIRouter()

@router.get("/query/")
async def query_documents(query: str = Query(..., min_length=1)):
    try:
        print(f" Received query: {query}")

        results = await search_documents(query)

        if not results or results == ["No documents matched your query."]:
            return {
                "results": [],
                "message": " No relevant documents found."
            }

        return {
            "results": results,
            "message": f"Found {len(results)} matching document(s)."
        }

    except Exception as e:
        print(f" Error in query_documents: {e}")
        return {
            "results": [],
            "error": str(e),
            "message": " Failed to process query."
        }


