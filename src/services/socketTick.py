from websocket import WebSocketApp
import threading
import ssl
import time


class socketTick:
    def __init__(self, url='ws://echo.websocket.events/', count=5):
        self.ws = None
        self.url = url
        self.count = count

    def on_message(self, ws, message):
        print('Received: ' + message)
        self.count -= 1
        if 0 == self.count:
            ws.close()

    def on_open(self, ws):
        def gao():
            for i in range(5):
                time.sleep(0.01)
                msg = "{0}".format(i)
                ws.send(msg)
                print('Sent: ' + msg)
            time.sleep(1)
            ws.close()
            print('ws close...')

        threading.Thread(target=gao).start()

    def start(self):
        print('ws start...')
        # 使用默认url，调用的方法
        if 'ws://echo.websocket.events/' == self.url:
            self.ws = WebSocketApp(self.url,
                                   on_open=self.on_open,
                                   on_message=self.on_message)
            self.ws.run_forever(ping_timeout=10)
        else:
            self.ws = WebSocketApp(self.url,
                                   on_message=self.on_message)
            self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


