from flask import Flask, request, Response, abort, send_file, send_from_directory, jsonify
from functools import wraps
import os
import sqlite3
import base64
from OpenSSL import SSL

app = Flask(__name__)


def connDB():
    return sqlite3.connect('database.db')


def initDB():
    conn = connDB()
    c = conn.cursor()
    c.execute(''' CREATE table if not exists messages(
                        Message varchar(255),
                        Name varchar(255)
                    ); ''')
    conn.commit()


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'guest' and password == 'password'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials\n',
        401)


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route('/', methods=['GET'])
def home():
    return 'In header: {}'


@app.route('/message/<username>', methods=['POST'])
@requires_auth
def sendMessage(username):
    content = request.get_json(force=True)

    message = content["message"]

    print("trying to commit with message: {}\nusername: {}".format(message, username))

    conn = connDB()
    c = conn.cursor()
    c.execute(''' INSERT into messages (Message, Name) 
                  VALUES ('{}', '{}')'''.format(message, username))
    conn.commit()
    return "\nSuccess!\n"


@app.route('/messages', methods=['GET'])
@requires_auth
def showMessages():
    conn = connDB()
    c = conn.cursor()
    c.execute(''' SELECT * FROM messages ''')

    msg = "<p>"
    for item in c.fetchall():
        msg += "{}: {}<br />\n".format(item[1], item[0])
    msg += "</p>"

    return msg


if __name__ == '__main__':
    initDB()
    context = ('server.crt', 'server.key')
    app.run(port=8080, ssl_context=context)
