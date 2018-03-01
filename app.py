import os

from flask import Flask, render_template, request, redirect, url_for, Response
from flask_socketio import SocketIO, emit
app = Flask(__name__)

server_data = {}
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def index():
    #return render_template('index.html', users=User.query.all())
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    print('Received data from client: %s' % request.args.get("test"))
    return Response(request.args.get("test"))

@socketio.on('aaa')
def test_connect():
    print("Welcome, aaa received")
    emit('aaa_response', {'data': 'Server'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(host='0.0.0.0', port=port, debug=True)
