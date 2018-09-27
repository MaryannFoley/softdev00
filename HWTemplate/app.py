from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def something():
    return "<h3>Homework template</h3>"
    #render_template is also useful

if __name__ == "__main__":
    app.debug = True
    app.run()
