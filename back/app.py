"""
Refs:
- https://gabrielcp.medium.com/realtime-chat-with-flask-socket-io-and-angular-c14f32a240f0
"""
import time
from threading import Thread

from flask import Flask, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask_cors import CORS
from loguru import logger as log


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"

# Fix CORS
# https://stackoverflow.com/questions/29187933/flask-socketio-cors
socketio = SocketIO(app, cors_allowed_origins="*")

CORS(app)
users = {}


# @socketio.on("sign_in")
# def user_sign_in(user_name):
#     users[request.sid] = user_name["name"]  # type: ignore
#     socketio.emit("current_users", users)
#     log.debug(f"User sign in: {user_name['name']}") 
#     log.debug(f"Users now: {users}")


@socketio.on("connect")
def on_connect():
    print("User connect")


@socketio.on("disconnect")
def on_disconnect():
    print("User disconnect")


@socketio.on("join")
def join(message):
    print(f"Message on join: {message}")
    join_room("sensor")
    Thread(target=thread_data).start()


@socketio.on("message")
def messaging(message):
    print(f"Receive message: {message}")
    socketio.emit("message", {"message": message, "i_love_pizza": True})
    # message["from"] = request.sid
    # socketio.emit("message", message, room=request.sid)
    # socketio.emit("message", message, room=message["to"])


def thread_data():
    while True:
        time.sleep(2)
        print("Send data")
        import random
        socketio.send(str(random.randint(0,100)), to="sensor")

if __name__ == "__main__":
    app.run(port=8000)
