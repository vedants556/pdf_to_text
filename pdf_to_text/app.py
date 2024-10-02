from flask import Flask, request, render_template
import os
import fitz  # PyMuPDF

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', error="No file part")
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error="No selected file")
    
    if not file.filename.endswith('.pdf'):
        return render_template('index.html', error="Unsupported file format. Please upload a PDF file.")

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    try:
        text = extract_text_from_pdf(filepath)
        return render_template('result.html', text=text)
    except Exception as e:
        return render_template('index.html', error=f"An error occurred: {str(e)}")

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

if __name__ == '__main__':
    app.run(debug=True)
