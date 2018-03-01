import os

from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret1'

erver_data = {}

@app.route('/', methods=['GET'])
def index():
  #return render_template('index.html', users=User.query.all())
  return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    print('Received data from client: %s' % request.data)
    return Response('')

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  socketio = SocketIO(app)
  socketio.run(host='0.0.0.0', port=port, debug=True)
