import flask
import os.path
import ipaddr
import errno

app = flask.Flask(__name__)
cwd = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.abspath(os.path.join(cwd, 'addresses'))

def record_new_ip(i):
    # If it is insane in format, just crash.
    try:
        parsed = ipaddr.IPv4Address(i)
    except ValueError:
        return

    as_str = str(parsed)

    path = os.path.join(data_dir, as_str)
    try:
        os.mkdir(path)
    except OSError, e:
        if e.errno != errno.EEXIST:
            raise

def get_addresses():
    if os.path.exists(data_dir):
        return os.listdir(data_dir)

@app.route('/')
def show_ips():
    ip = flask.request.remote_addr
    return flask.render_template(
        'index.html',
        addresses=get_addresses(),
        ip=ip)

@app.route('/add-yourself/')
def add_yourself():
    ip = flask.request.remote_addr
    record_new_ip(ip)
    return flask.redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100)

