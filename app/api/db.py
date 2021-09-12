import click
from flask import current_app, g
from flask.cli import with_appcontext
import mysql.connector
from .schema import instructions


class DatabaseManager:
    def get_db(self):
        if 'db' not in g:
            g.db = mysql.connector.connect(
                    host=current_app.config['MYSQL_HOST'],
                    user=current_app.config['MYSQL_USER'],
                    password=current_app.config['MYSQL_PASSWORD'],
                    database=current_app.config['MYSQL_DATABASE']
                    )
            g.c = g.db.cursor(dictionary=True)

            return g.db, g.c

    def close_db(self, e=None):
        db_connect = g.pop('db', None)

        if db_connect is not None:
            db_connect.close()

    def init_db(self):
        db_connect, db_cursor = self.get_db()

        for i in instructions:
            db_cursor.execute(i)
        db_connect.commit()


connector = DatabaseManager()


@click.command('init-db')
@with_appcontext
def init_db_command():
    connector.init_db()


def init_app(app):
    app.teardown_appcontext(connector.close_db)
    app.cli.add_command(init_db_command)
