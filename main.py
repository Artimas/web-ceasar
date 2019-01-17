from flask import Flask, request
from ceasar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
            margin: 10px 0;
            width: 540px;
            height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label>
                Rotate by:<input type="text" name="rot" id="rot" />
            </label>
            <textarea name="text" id="text">{0}</textarea>
            <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>        
"""

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form["rot"]
    if not is_integer(rot):
        return "Not a valid integer"
    else:
        rot = int(rot)
    text = request.form["text"]
    encrypted_text = rotate_string(text, rot)
    return form.format(encrypted_text)

@app.route("/")
def index():
    return form.format("")


app.run()