from PIL import Image
import pytesseract
import pdfplumber

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
    except Exception as e:
        print(f"PDF Error ({pdf_path}): {e}")
    return text

# Function to extract text from image using OCR
def extract_text_from_image(image_path: str) -> str:
    text = ""
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
    except Exception as e:
        print(f"Image Error ({image_path}): {e}")
    return text
