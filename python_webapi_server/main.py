import time
from http.server import HTTPServer
from python_webapi_server.server import Server


PORT = 8080
HOST_NAME = 'localhost'

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME,PORT), Server)
    print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
        httpd.server_close()
        print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT))

