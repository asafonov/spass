import uuid, os, pwd, socket

def get_device_id():
    return get_hostname()

def get_username():
    return pwd.getpwuid(os.getuid()).pw_name

def get_userid():
    return os.getuid()

def get_hostname():
    return socket.gethostname()
