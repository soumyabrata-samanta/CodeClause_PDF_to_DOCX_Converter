from flask import Flask,render_template,url_for,request,redirect,send_file
from pdf2docx import Converter

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/convert', methods=['POST'])
def convert_pdf_to_docx():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    pdf_file = request.files['file']
    if pdf_file.filename == '':
        return 'No file selected', 400
    pdf_path = 'uploaded_file.pdf'
    pdf_file.save(pdf_path)

    try:
        docx_path = 'converted_file.docx'
        cv = Converter(pdf_path)
        cv.convert(docx_path)
        cv.close()
        return send_file(docx_path, as_attachment=True, download_name='converted_file.docx')
    except Exception as e:
        return str(e), 500

if __name__== "__main__":
    app.run(debug=True)
