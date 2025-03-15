from flask import, render_template
import os


p_list = [("Віктор","Київ"),
          ("Володимир","Київ"),
          ("Юлія","Одеса"),
          ("Микола","Луцьк"),
          ("Іван","Київ"),
          ("Петро","Рівне")]
def index():
    return render_template("index.html")


folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder)


app.add_url_rule("/", "index", index)


if __name__ == "__main__":
    app.run()
