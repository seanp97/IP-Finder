import socket
import sys
import pyperclip

class IP:

    def __init__(self):
        if len(sys.argv) > 0:
            self._url = sys.argv[1]
            self.get_ip(self._url)


    def get_ip(self, url):
        if "https://" in url:
            url = url.replace("https://", "")
            self.last_char = url[len(url) - 1]
            if self.last_char == "/":
                url = url.replace("/", "")

        elif "http://" in url:
            url = url.replace("http://", "")
            self.last_char = url[len(url) - 1]
            if self.last_char == "/":
                url = url.replace("/", "")

        self.ip = socket.gethostbyname(url)
        print(self.ip)
        pyperclip.copy(self.ip)


IP()