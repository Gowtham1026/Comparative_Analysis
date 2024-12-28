from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

def perform_comparative_analysis(file1, file2):
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)
    
    comparison = df1.compare(df2, keep_shape=True, keep_equal=True)
    
    return comparison.to_html(classes="table table-striped")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file1 = request.files["file1"]
        file2 = request.files["file2"]
        
        if file1 and file2:
            result = perform_comparative_analysis(file1, file2)
            return render_template("index.html", result=result)
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
