from datetime import datetime
from dateutil.relativedelta import relativedelta


class Repository:
    ROW_HEADER = [
        "id",
        "name_with_owner",
        "url",
        "stargazer_count",
        "pull_requests",
    ]

    def __init__(self, repo_json=None, repo_row=None):
        if repo_json is not None:
            self.id = repo_json["id"]
            self.name_with_owner = repo_json["nameWithOwner"]
            self.url = repo_json["url"]
            self.stargazer_count = repo_json["stargazerCount"]
            self.pull_requests = repo_json["pullRequests"]["totalCount"]

        if repo_row is not None:
            self.id = repo_row[self.ROW_HEADER[0]]
            self.name_with_owner = repo_row[self.ROW_HEADER[1]]
            self.url = repo_row[self.ROW_HEADER[2]]
            self.stargazer_count = repo_row[self.ROW_HEADER[3]]
            self.pull_requests = repo_row[self.ROW_HEADER[4]]

    def get_string_row(self):
        return [
            self.id,
            self.name_with_owner,
            self.url,
            self.stargazer_count,
            self.pull_requests,
        ]
