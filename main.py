from user import User
from data_managment import Manager
from log import Log
import datetime

user = None
log = Log()

def time_n_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%I:%M:%S")
    return current_date, current_time
try:
    date, time = time_n_date()
    manager = Manager()
    user = User(manager)
    msg = f"[{date} / {time}] -> Success\n"
    log.success(msg)
    user.root.mainloop()

except Exception as e:
    date, time = time_n_date()
    msg = f"[{date} / {time}] -> {type(e).__name__}: {e}\n"
    log.error(msg)