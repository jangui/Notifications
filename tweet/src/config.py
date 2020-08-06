import os

class Config:
    SECRET_KEY = os.urandom(32)

    def __init__(self):
        if os.environ.get('DEBUG', None):
            self.DEBUG = True

