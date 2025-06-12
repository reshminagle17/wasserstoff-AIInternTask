from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class TextInput(BaseModel):
    text: str

{
  "themes": ["Programming / AI / ML"]
}

# Improved multi-theme identification function
def identify_themes(text: str) -> List[str]:
    text = text.lower()
    themes = []

    education_keywords = ["student", "exam", "university", "school", "assignment"]
    finance_keywords = ["invoice", "payment", "transaction", "amount", "balance"]
    healthcare_keywords = ["doctor", "medicine", "hospital", "treatment", "health"]
    programming_keywords = ["python", "oop", "pandas", "numpy", "machine learning", "function", "loop", "code"]

    if any(word in text for word in education_keywords):
        themes.append("Education")
    if any(word in text for word in finance_keywords):
        themes.append("Finance")
    if any(word in text for word in healthcare_keywords):
        themes.append("Healthcare")
    if any(word in text for word in programming_keywords):
        themes.append("Programming / AI / ML")

    if not themes:
        themes.append("General")

    return themes


# Updated route
@router.post("/identify-theme")
async def get_theme(input: TextInput):
    themes = identify_themes(input.text)
    return {"themes": themes}

