from flask import Flask, render_template, request

app = Flask(__name__)

# Define the votes dictionary
votes = {
    "Ather": 0,
    "Access 125": 0,
    "Chetak": 0,
    "RE Hunter 350": 0
}

@app.route("/", methods=['GET', 'POST'])
def vote():
    choice = None
    winner = None

    if request.method == 'POST':
        # Must match HTML form input name
        choice = request.form.get('bike')
        if choice in votes:
            votes[choice] += 1

    # Determine current leader
    if votes:
        winner = max(votes, key=votes.get)

    # Pass votes and winner to template
    return render_template('index.html', choice=choice, votes=votes, winner=winner)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005)

