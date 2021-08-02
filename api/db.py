import click
from flask import current_app, g
from flask.cli import with_appcontext
import mysql.connector
from .schema import instructions


def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            database=current_app.config['MYSQL_DB']
                )
        g.c = g.db.cursor(dictionary=True)

        return g.db, g.c


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i)
    db.commit()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Database tables created')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
