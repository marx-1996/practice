from flask import Flask, render_template, request, send_file

from pdf_generator import generate_pdf



app = Flask(__name__)



@app.route("/")
def home():

    return render_template(
        "index.html"
    )



@app.route("/create", methods=["POST"])
def create():


    text = request.form["content"]


    cols = int(
        request.form["cols"]
    )


    style = request.form["style"]




    filename = generate_pdf(
    text,
    cols,
    style
)


    return send_file(

        filename,

        as_attachment=True,

        download_name="練字字帖.pdf",

        mimetype="application/pdf"

    )



if __name__ == "__main__":

    app.run(debug=True)