from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
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
        <form action="/" method="post">
            <label for="rotate-by">Rotate by:</label>
            <input id="rotate-by" type="text" name="rot" value="0"/>
            <br>
            <textarea name="text">{0}</textarea>
            <br>
            <input type="submit" />
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

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rotate  = request.form['rot']
    text_box = request.form['text']
    cipher = rotate_string(text_box, int(rotate))


    if is_integer(rotate): 
        return '<h1>' + form.format(cipher) + '</h1>'
    else:
        return '<h1>This is not a valid integer</h1>'

app.run()