from flask import Flask, render_template
app = Flask(__name__, static_folder='static')


@app.route('/')
def home():
    title = 'welcome'
    return render_template('home.html', title=title)


@app.route('/about/')
def about():
    return 'This is the about page. Hello!'

# We doing Sudoku Solver 







if __name__ == '__main__':
    app.run(debug=True)

