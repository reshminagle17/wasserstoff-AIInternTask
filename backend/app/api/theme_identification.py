from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class TextInput(BaseModel):
    text: str

# Improved multi-theme identification function
def identify_themes(text: str) -> List[str]:
    text = text.lower()
    themes = []

    education_keywords = ["student", "exam", "university", "school", "assignment","python","code","programming","learning","developer","interview","projects","function","oops","syntax","library"]
    finance_keywords = ["invoice", "payment", "transaction", "amount", "balance"]
    healthcare_keywords = ["doctor", "medicine", "hospital", "treatment", "health"]

    if any(word in text for word in education_keywords):
        themes.append("Education")
    if any(word in text for word in finance_keywords):
        themes.append("Finance")
    if any(word in text for word in healthcare_keywords):
        themes.append("Healthcare")

    if not themes:
        themes.append("General")

    return themes

# Updated route
@router.post("/identify-theme")
async def get_theme(input: TextInput):
    themes = identify_themes(input.text)
    return {"themes": themes}

