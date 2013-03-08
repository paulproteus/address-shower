import flask
import os

app = flask.Flask(__name__)
cwd = os.path.dirname(os.path.abspath(__file__))

def record_new_ip(i):
    # If it is insane in format, just crash.
    pass

def get_addresses():
    '''A total placeholder for now.'''
    return [
        '192.168.1.2',
        '10.0.0.1',
        ]

@app.route('/')
def show_ips():
    return flask.render_template(
        'index.html',
        addresses=get_addresses())

if __name__ == '__main__':
    app.run()

