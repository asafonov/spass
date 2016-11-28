import uuid, os, pwd

def get_device_id():
    return uuid.getnode()

def get_username():
    return pwd.getpwuid(os.getuid()).pw_name

def get_userid():
    return os.getuid()
