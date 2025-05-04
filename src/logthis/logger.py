import datetime

def _timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_info(message: str):
    print(f"\033[92m[{_timestamp()}] [INFO] {message}\033[0m")

def log_warn(message: str):
    print(f"\033[93m[{_timestamp()}] [WARN] {message}\033[0m")

def log_error(message: str):
    print(f"\033[91m[{_timestamp()}] [ERROR] {message}\033[0m")