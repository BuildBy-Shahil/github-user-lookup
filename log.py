import os

class Log:
    def __init__(self):
        if not os.path.exists("logs"):
            os.makedirs("logs", exist_ok=True)

    def success(self, scc_msg):
        with open("logs/git.log", "a") as scc:
            scc.write(scc_msg)


    def error(self, err_msg):
        with open("logs/git.log", "a") as err:
            err.write(err_msg)