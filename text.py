import csv

def baca_data_csv(nama_file = 'data_lagu.csv'):
    data = []
    with open(nama_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# @app.route("/main")
# def index1():
#         return render_template("main.html")

# @app.route("/redirect")
# def redirect():
#         return redirect(url_for('index'))

# @app.route("/")
# def index():

#     # looping
#     day = ['sunday','monday','tuesday' ]

#     #if else
#     ee = "sad" 
#     value = 1
#     return render_template("index.html", value= day, valuee = ee)

# @app.route("/main")
# def main():
#     return render_template("main.html")


# @app.route("/parsing/<int:value>")
# def parsing(value):
#     return "value is: {}".format(value)


# @app.route("/argumen")
# def argum():
#     data = request.args.get("value")
#     return "sasasa {}" .format(data) 

# # session
# @app.route("/page/<int:value>")
# def page(value):
#     session["value"] = value
#     return "success"

# @app.route("/page/detail")
# def view_sesion():
#     data = session["value"]
#     return "value is: {}".format(data)

# # logout
# @app.route("/page/logout")
# def logout_sesion():
#     session.pop("value")
#     return "berhasil logout"