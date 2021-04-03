from datetime import datetime
from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    db_session.global_init("db/mars.db")
    db_sess = db_session.create_session()
    jobs = [job for job in db_sess.query(Jobs).all()]
    users = [user for user in db_sess.query(User).all()]
    return render_template('works_journal.html', title='Journal works', 
                           jobs=jobs, users=users)


def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()


'''@app.route('/training/<prof>')


def training(prof):
    return render_template('training.html', prof=prof)'''

