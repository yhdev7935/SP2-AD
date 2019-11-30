import socket, urllib.request

def InternetConnected():
    ip = socket.gethostbyname(socket.gethostname())
    if ip == "127.0.0.1":
        return False
    else:
        return True

def getServerVersion():
    url = "https://raw.githubusercontent.com/yhdev7935/SP2-AD/master/VERSION"
    data = urllib.request.urlopen(url)
    return str(data.read().decode('utf-8'))


if __name__ == "__main__":
    print(getServerVersion())