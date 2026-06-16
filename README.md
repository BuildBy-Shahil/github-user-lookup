## GitHub User Lookup Tool

Python application that retrieves GitHub user information through the GitHub API and stores results in SQLite.

## Features

- GitHub username lookup
- GitHub API integration
- JSON response parsing
- SQLite database storage
- Data retrieval from database
- Error logging
- Export functionality


## Technologies Used

- Python
- Requests
- tkinter
- SQLite
- JSON
- CSV

## JSON Response

{
    "id": 1,
    "login": "example_name",
    "name": example_name,
    "profile_url": "https://github.com/example_name",
    "followers": "16",
    "following": "0",
    "public_repos": "0",
    "checked_time": "example_checked date/time | 2026-06-12 / 09:33:10"
}

## Data Source

This project retrieves public user information from the GitHub REST API.

Example endpoint:

https://api.github.com/users/{username}