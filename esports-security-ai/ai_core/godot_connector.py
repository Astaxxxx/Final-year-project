import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5555")

def send_alert(status):
    socket.send_string(status)

# Example Usage
send_alert("threat_detected")
