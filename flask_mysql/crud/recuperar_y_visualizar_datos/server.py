from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Una lista inicial de amigos ficticios
friends = []

class Friend:
    def __init__(self, name):
        self.name = name

    @classmethod
    def get_all(cls):
        return friends

@app.route('/')
def index():
    return render_template("index.html", all_friends=Friend.get_all())

@app.route('/add_friend', methods=['POST'])
def add_friend():
    if request.method == 'POST':
        new_friend_name = request.form['new_friend']
        if new_friend_name:
            new_friend = Friend(new_friend_name)
            friends.append(new_friend)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
