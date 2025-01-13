from flask import Flask
from flask import render_template, request

#WSGI Application
app = Flask(__name__)
'''
It creates an instance of a flask class, whcih will be your Web server gateway interface
'''

@app.route('/')
def home():
    return 'Welcome to flask application'

@app.route('/render_template')
def renderer():
    return render_template('index.html') #File must be in templates folder

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method=='POST':
        name = request.form['name']
        return f'Hello {name}!' 
    return render_template('form.html')

#Variable Rule
@app.route('/success/<int:score>/')
def success(score):
    res = ''
    if score>50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    exp = {
        'result':res,
        'score':score
    }
    
    return render_template('result.html', result = res, results=exp)

'''
Jinja2 templating engine
{{  }} expressions to print out output in html
{%...%} conditions, for loops
{#...#} for comments
'''

if __name__ == '__main__':
    app.run(debug=True)