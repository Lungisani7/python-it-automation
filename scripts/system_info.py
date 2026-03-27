import platform
import socket
import os

def get_system_info():
    print("=== SYSTEM INFORMATION ===")
    print(f"Computer Name: {socket.gethostname()}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"OS Version: {platform.version()}")
    print(f"Processor: {platform.processor()}")
    print(f"Architecture: {platform.architecture()[0]}")
    print(f"Current User: {os.getlogin()}")

if __name__ == "__main__":
    get_system_info()
