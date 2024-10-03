from PIL import Image
import pytesseract
from openpyxl import Workbook
import re

# Path to tesseract executable (update if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\danie\Desktop\Github_Tools\OCR_windows\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    # Load the image
    img = Image.open(image_path)
    
    # Perform OCR
    text = pytesseract.image_to_string(img)
    
    return text

def extract_items_and_prices(text):
    # Example regular expression to capture items and prices
    pattern = r'([A-Za-z\s]+)\s+(\d+\.\d{2})'
    matches = re.findall(pattern, text)
    
    # Print extracted items and prices
    for item, price in matches:
        print(f"Item: {item}, Price: {price}")
    
    return matches

def write_to_excel(data, excel_path='receipt_data.xlsx'):
    wb = Workbook()
    ws = wb.active
    
    # Write headers
    ws.append(["Item", "Price"])
    
    # Write data
    for item, price in data:
        ws.append([item.strip(), price])
    
    # Save Excel file
    wb.save(excel_path)

# Main function to process the receipt
def process_receipt(image_path):
    text = extract_text_from_image(image_path)
    parsed_data = extract_items_and_prices(text)
    write_to_excel(parsed_data)

# Run the tool
if __name__ == "__main__":
    image_path = 'receipt.jpg'  # Replace with your receipt image file path
    process_receipt(image_path)
