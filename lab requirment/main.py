from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/input')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    sentence = request.form['sentence']
    res = sentence.upper()
    return render_template('result.html', result=res)
if __name__ == "__main__":
    app.run(debug=True)
