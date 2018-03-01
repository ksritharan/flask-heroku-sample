import os

from flask import Flask, render_template, request, redirect, url_for, Response
from flask_socketio import SocketIO, emit

try:
    import Queue as queue
except:
    import queue

app = Flask(__name__)

server_data = {}
server_queue = queue.Queue()
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
def receive_data(data):
    print("Received: %s" % str(data))
    server_queue.put(data['data'])

t = None
@socketio.on('bbb')
def send_data():
    global t
    if t is None:
        t = socketio.start_background_task(target=phone_handler)

def phone_handler():
    while 1:
        data = server_queue.get(True)
        socketio.emit("bbb_response", {'data': data})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(host='0.0.0.0', port=port, debug=True, async_mode='threading')
