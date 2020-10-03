import random
user = "MOJI"
from flask import Flask, render_template
app = Flask(__name__,template_folder='template')
@app.route('/')
def index():
    global user
    return render_template('index.html', name = user,img_path = random.choice(["img_chania.jpg","test.jpg"]))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
