from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('signin.html')

@app.route('/myExpense')
def myExpense():
    return render_template('index.html')

@app.route('/myPay')
def myPay():
    return render_template('pay.html')

@app.route('/collab_signin')
def collab_signin():
    return render_template('collaboration_signin.html')

@app.route('/collab')
def collab():
    return render_template('collaborations.html')

@app.route('/collabPay')
def collabPay():
    return render_template('collaboration_pay.html')

if __name__ == '__main__':
    app.run(debug=True)
