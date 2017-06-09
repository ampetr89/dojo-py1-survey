from flask import Flask, render_template, redirect, request

app = Flask(__name__)

params = {
	'dc': 'Washington D.C.',
	'sj': 'San Jose',
	'chi': 'Chicago',
	'py': 'Python',
	'sql': 'SQL',
	'js': 'JavaScript'
}
params.setdefault('','')

@app.route('/')
def index():	
	return render_template('index.html', **params)


@app.route('/result', methods=['POST'])
def result():
	names = ['name', 'location', 'lang', 'comment']
	responses = request.form.copy()
	for name in names:
		responses.setdefault(name, '') # use an empty string if the user didn't enter anything

	vals = {
		'name': responses['name'],
		'location': params[responses['location']],
		'lang': params[responses['lang']],
		'comment': responses['comment']
	}

	if responses['lang']:
		print('non empty language')
		vals['lang'] += '!!!'
	
	return render_template('result.html', **vals)


app.run(debug=True)