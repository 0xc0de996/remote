import sys
import zmq
import cv2
import numpy as np


arg = sys.argv
ip = arg[1]
port = arg[2]

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://{ip}:{port}")  

socket.setsockopt_string(zmq.SUBSCRIBE, "")

while True:
    image_data = socket.recv()
    nparr = np.frombuffer(image_data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow('Screen', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
