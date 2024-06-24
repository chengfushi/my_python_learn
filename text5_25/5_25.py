# import socket
#
# sock = socket.socket()
# sock.bind(("127.0.0.1", 7777))
# sock.listen(3)
#
# print("服务器已启动..")
# while True:
#     conn, addr = sock.accept()
#     data = conn.recv(1024)
#     print("收到请求:", data.decode())
#
#     response = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
#     <h1>Hello, World!</h1>
#     <img src='https://img0.baidu.com/it/u=4011424408,4733765&fm=253&fmt=auto&app=138&f=JPEG?W=500&h=750'>"""
#
#     conn.sendall(response.encode())
#     conn.close()

# from flask import Flask, render_template
# import datetime
#
# app = Flask(__name__, template_folder="templates")
#
# @app.route("/index")
# def index():
#     return render_template("index.html")
#
# @app.route("/timer")
# def timer():
#     now = datetime.datetime.now().strftime("%Y-%m-%d %X")
#     return render_template("timer.html", now=now)
#
# app.run()
