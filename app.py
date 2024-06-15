from flask import Flask, render_template
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    emit('message', 'Mit Baabocrypt-Server verbunden')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

# when a message comes in, broadcast
@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    # turn data into json
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5333, debug=True)