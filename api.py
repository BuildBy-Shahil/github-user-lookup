import requests
from datetime import datetime
from log import Log

def get_date_time():
    """Get current Date and Time"""
    now = datetime.now()
    checked_time = now.strftime("%I:%M:%S")
    checked_date = now.strftime("%Y-%m-%d")
    return checked_date, checked_time

class API:
    def __init__(self, manager):
        self.manager = manager

    def get_api_data(self, name):
        try:
            checked_date, checked_time = get_date_time()

            data = requests.get(f"https://api.github.com/users/{name}")

            if data.status_code != 200:
                raise Exception(f"API Failed: {data.status_code}")

            user_data = data.json()
            user_info_dict = {
                "login": user_data["login"],
                "name": user_data["name"],
                "profile_url": user_data["html_url"],
                "followers": user_data["followers"],
                "following": user_data["following"],
                "public_repos": user_data["public_repos"],
                "checked_time": f"{checked_date} / {checked_time}"
            }
            self.manager.insert(user_info_dict)
        except Exception as e:
            log = Log()
            date, time = get_date_time()
            msg = f"[{date} / {time}] -> {type(e).__name__}: {e}\n"
            log.error(msg)
            exit() # Close everything if exception happens
