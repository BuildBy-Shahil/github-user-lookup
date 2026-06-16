import os
import sqlite3
from tkinter import filedialog
import csv
import json

def convert_to_csv(data, path):
    # Have to fix this
    user_data = []
    for d in data:
        user_data.append({
            "Login": d[1],
            "Name": d[2],
            "Profile_url": d[3],
            "Followers": d[4],
            "Following": d[5],
            "Public_repos": d[6],
            "Checked_time": d[7],
        })

    with open(path, "w", newline="", encoding="utf-8") as file:
        field_name = ["Login", "Name", "Profile_url", "Followers", "Following", "Public_repos", "Checked_time"]
        writer = csv.DictWriter(file, field_name)
        writer.writeheader()
        for data in user_data:
            writer.writerow(data)

def convert_to_text(data, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(data)

class Manager:
    def __init__(self):
        self.path = os.getenv("APPDATA")
        self.folder = os.path.join(self.path, "git_user")

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        self.db_file = os.path.join(self.folder, "git_users.db")

        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS git_user_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT,
                name TEXT UNIQUE,
                profile_url TEXT,
                followers TEXT,
                following TEXT,
                public_repos TEXT,
                checked_time TEXT
            )
        """)


    def insert(self, user_data):
        query = """INSERT OR IGNORE INTO git_user_data (login, name, profile_url, followers, following, public_repos, checked_time) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        self.cursor.execute(query,
                            [
                                user_data["login"],
                                user_data["name"],
                                user_data["profile_url"],
                                user_data["followers"],
                                user_data["following"],
                                user_data["public_repos"],
                                user_data["checked_time"]
                            ]
                            )
        self.conn.commit()

    def fetch(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=(("txt Files", "*.txt"), ("csv Files", "*.csv"), ("All Files", "*.*")),
            title="Save File"
        )
        if path:
            self.cursor.execute("""SELECT *
                                   FROM git_user_data""")
            rows = self.cursor.fetchall()
            columns = [col[0] for col in self.cursor.description]
            data = [dict(zip(columns, row)) for row in rows]
            list_of_data = [d for d in data]
            user_data_json_formate= json.dumps(list_of_data, indent=4)

            if ".txt" in path:
                """If user save file as text"""
                convert_to_text(user_data_json_formate, path)

            elif ".csv" in path:
                """If user save file as csv"""
                convert_to_csv(rows, path)