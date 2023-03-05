import socket


def getIP():
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    SOCKET.settimeout(0)
    
    try:
        SOCKET.connect(("10.254.254.254", 1))
        IP = SOCKET.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        return IP