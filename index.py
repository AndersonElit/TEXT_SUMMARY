from flask import Flask, render_template, request, redirect, url_for
from SummaryText import TextSummary

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    texto = request.form.get('text')
    resumen = TextSummary(texto)
    return render_template('text_sum.html', texto=texto, resumen=resumen)

@app.route('/reset')
def reset():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)