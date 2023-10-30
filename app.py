from flask import Flask, request, Response, render_template, redirect,url_for
import pandas as pd
from vcfGenerator import generate

app = Flask(__name__)

@app.route("/",methods={"GET"})
def home():
    return render_template("upload.html")

@app.route('/upload', methods=['POST',"GET"])
def uploadFile():

    if 'file' not in request.files:
        return "Please upload a file"

    file = request.files['file']

    if file and file.filename.endswith('.csv'):
        
        df=pd.read_csv(file)
        vcardString = generate(df)        
        response = Response(vcardString, content_type='text/vcard')
        response.headers['Content-Disposition'] = 'attachment; filename=contacts.vcf'
        return response

    else:
        return 'Invalid file format. Please upload a CSV file.'


if __name__ == '__main__':
    app.run(debug=True)
