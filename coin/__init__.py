import threading
from . import jobs

threading.Timer(3, jobs.countSeconds).start()