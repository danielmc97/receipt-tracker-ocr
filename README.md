# Receipt Tracker OCR

A Python tool that uses Optical Character Recognition (OCR) to extract item names and prices from a receipt image and automatically inputs the data into an Excel spreadsheet. This project utilizes `Tesseract OCR`, `PIL`, and `openpyxl` libraries to handle image processing and Excel file creation.

## Features
- Extract item names and prices from a receipt image.
- Save the extracted data into an Excel spreadsheet.
- Handles common receipt formats with item and price pairs.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
- **Python 3.x**: Make sure you have Python installed. You can download it [here](https://www.python.org/downloads/).
- **Tesseract OCR**: You need to have Tesseract installed on your machine.
    - [Tesseract OCR installation guide](https://github.com/tesseract-ocr/tesseract/wiki)
    - Once installed, set the correct path in the code:
      ```python
      pytesseract.pytesseract.tesseract_cmd = r'path\to\tesseract.exe'
      ```

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/receipt-tracker-ocr.git
    cd receipt-tracker-ocr
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/Scripts/activate  # Windows
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up Tesseract OCR:
    - Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
    - Update the path in the `ocr_tool.py` file:
      ```python
      pytesseract.pytesseract.tesseract_cmd = r'C:\path\to\tesseract.exe'
      ```

## Usage

1. Place your receipt image in the project folder.
2. Open a terminal in the project folder and run the following command:
    ```bash
    python ocr_tool.py
    ```

3. The extracted data will be printed in the terminal and saved in an Excel file (`receipt_data.xlsx`) in the project folder.

### Example Output
If the image contains the following text:
