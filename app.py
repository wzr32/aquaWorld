from flask import Flask, render_template, url_for, request, redirect
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd9242cfadfe7b70a7c202667524c724a'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    applicant_form = Applicant()
    if applicant_form.validate_on_submit():
        print(applicant_form.status.data)
        return redirect(url_for('index'))

    return render_template('apply.html', applicant_form=applicant_form)

if __name__=='__main__':
    app.run(debug=True)