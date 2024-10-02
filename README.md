# PDF to Text Converter

## Description

PDF to Text Converter is a web application built with Flask that allows users to upload PDF files and extract the text content. This tool is useful for quickly converting PDF documents into plain text format, making it easier to copy, paste, and manipulate the content.

## Features

- User-friendly web interface
- PDF file upload functionality
- Text extraction from PDF files
- Display of extracted text
- Copy to clipboard functionality
- Responsive design for various screen sizes

## Technologies Used

- Python 3.x
- Flask (Web Framework)
- PyMuPDF (PDF processing library)
- HTML/CSS
- Bootstrap 5 (Frontend framework)
- Font Awesome (Icons)

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/pdf-to-text-converter.git
   cd pdf-to-text-converter
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install flask PyMuPDF
   ```

4. Run the application:
   ```
   python pdf_to_text/app.py
   ```

5. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. On the home page, click the "Choose PDF" button to select a PDF file from your computer.
2. Click the "Convert to Text" button to upload the file and extract its text.
3. The extracted text will be displayed on the result page.
4. You can copy the text to your clipboard by clicking the "Copy Text" button.
5. To convert another PDF, click the "Upload Another PDF" button.

## Project Structure

```
pdf-to-text-converter/
│
├── pdf_to_text/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   └── uploads/  (created automatically)
│
└── README.md
```

## Error Handling

The application includes basic error handling for common issues such as:
- No file selected
- Unsupported file format (non-PDF files)
- General exceptions during text extraction

## Contributing

Contributions to improve the PDF to Text Converter are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)



