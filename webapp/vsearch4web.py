from flask import Flask, render_template
from my_vsearch import vsearch as vs

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello from Flask!'


@app.route('/search4')
def do_search() -> str:
    return str(vs.search4letters('life, the universe, and everything!', 'eiru,!'))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


app.run()
