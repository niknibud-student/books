from pydoc import HTMLDoc
from typing import NewType

from flask import Flask, escape, render_template, request
from vsearch import search_for_letters

app = Flask(__name__)

flask_request = NewType('flask_request', request)


def log_request(req: 'flask_request', res: str) -> None:  # type: ignore
    """
    Запись полученных данных в файл

    Args:
        req (request): запрос Flask
        res (str): ответ пользователю
    """
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/searchfor', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search_for_letters(phrase, letters))
    log_request(request, results)
    return render_template(
        'results.html',
        the_title=title,
        the_phrase=phrase,
        the_letters=letters,
        the_results=results
    )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':  # type: ignore
    return render_template('entry.html', the_title='Welcome to search_for_letters on the web')


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template(
        'viewlog.html',
        the_title='View Log',
        the_row_titles=titles,
        the_data=contents
    )


if __name__ == '__main__':
    app.run()
