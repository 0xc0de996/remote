import sys
import zmq
import mss

arg = sys.argv
ip = arg[1]
port = arg[2]

context = zmq.Context()
socket = context.socket(zmq.PUB)

socket.bind(f"tcp://{ip}:{port}")

with mss.mss() as sct:
    while True:
        screenshot = sct.shot(output='screen.png')  # 截取屏幕并保存为screen.png
        with open('screen.png', 'rb') as image_file:
            image_data = image_file.read()
        socket.send(image_data)
