from fastapi import APIRouter

router = APIRouter()

# Function to identify the theme based on the text
def identify_theme(text: str) -> str:
    text = text.lower()
    if "student" in text or "exam" in text:
        return "Education"
    elif "invoice" in text or "payment" in text:
        return "Finance"
    elif "doctor" in text or "medicine" in text:
        return "Healthcare"
    else:
        return "General"

# Route to get theme from text
@router.post("/identify-theme")
async def get_theme(text: str):
    theme = identify_theme(text)
    return {"theme": theme}
