from flask import Flask, render_template, request, redirect, url_for
from wand.image import Image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        input_pdf_path = request.form['pdf_file']
        if not input_pdf_path:
            return "Please select a PDF file."

        output_folder = 'C:/Newfolder/'
        base_output_name = 'output'
        counter = 1

        while True:
            output_pdf_path = os.path.join(output_folder, f'{base_output_name}{counter}.pdf')
            if not os.path.exists(output_pdf_path):
                break
            counter += 1

        with Image(filename=input_pdf_path, resolution=300) as img:
            img.format = 'pdf'
            img.background_color = 'white'
            img.alpha_channel = 'remove'
            img.save(filename=output_pdf_path)

        return f"Conversion successful. Output: {output_pdf_path}"

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
