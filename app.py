from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def vote():
    choice = None
    if request.method == 'POST':
        choice = request.form.get('vote')
    return render_template('index.html', choice=choice)

if __name__ == "__main__":
    # Changed from 5000 to 5005
    app.run(host='0.0.0.0', port=5005)
