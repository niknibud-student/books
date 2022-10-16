from pydoc import HTMLDoc
from typing import NewType

from flask import Flask, escape, render_template, request
from vsearch import search_for_letters

import sqlite3

app = Flask(__name__)


def log_request(req: 'request', res: str) -> None:  # type: ignore
    """
    Запись полученных данных в базу данных

    Args:
        req (request): запрос Flask
        res (str): ответ пользователю
    """
    dbconfig = {'database': 'vsearchlogdb.sqlite'}
    
    conn = sqlite3.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log
    (phrase, letters, ip, browser_string, results)
    values
    (?, ?, ?, ?, ?)"""
    '''
    print((req.form['phrase'],
        req.form['letters'],
        req.remote_addr,
        req.user_agent.string,
        res,))
    '''
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.string,
                          res,))
    conn.commit()
    cursor.close()
    conn.close()


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
def entry_page() -> str:
    return render_template('entry.html', the_title='Welcome to search_for_letters on the web')


@app.route('/viewlog')
def view_the_log() -> str:
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
