from flask import Flask, render_template, url_for,request, redirect
import os
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		nombre = data['nombre']
		email = data['email']
		mensaje = data['mensaje']

		file = database.write(f'\n{nombre},{email},{mensaje}')   


def write_to_csv(data):
	with open('database.csv',newline='',mode='a') as database2:
		nombre = data['nombre']
		email = data['email']
		mensaje = data['mensaje']
		
		csv_writer = csv.writer(database2, delimiter=',', quotechar='/', quoting= csv.QUOTE_MINIMAL)
		csv_writer.writerow([nombre,email,mensaje])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
         data = request.form.to_dict()
         write_to_csv(data)
         return redirect('/gracias.html')
      except:
     	 return 'No se guardó en la base de datos'

    else:
    	return 'Oh, rayos! Algo salió mal. Intenta de nuevo'