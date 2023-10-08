from datetime import datetime
from dateutil.relativedelta import relativedelta


class Repository:
    ROW_HEADER = [
        "id",
        "name_with_owner",
        "url",
        "created_at",
        "updated_at",
        "primary_language",
        "stargazer_count",
        "pull_requests",
        "releases",
        "issues_rate",
    ]

    def __init__(self, repo_json=None, repo_row=None):
        if repo_json is not None:
            self.id = repo_json["id"]
            self.name_with_owner = repo_json["nameWithOwner"]
            self.url = repo_json["url"]
            self.stargazer_count = repo_json["stargazerCount"]
            self.pull_requests = repo_json["details"]["pullRequests"]["totalCount"]
            self.releases = repo_json["details"]["releases"]["totalCount"]
            self.primary_language = "None"

            if repo_json["details"]["primaryLanguage"] is not None:
                self.primary_language = repo_json["details"]["primaryLanguage"]["name"]

            now = datetime.utcnow()

            created_at = datetime.strptime(repo_json["details"]["createdAt"], "%Y-%m-%dT%H:%M:%SZ")
            self.created_at = relativedelta(now, created_at).years

            updated_at = datetime.strptime(repo_json["details"]["updatedAt"], "%Y-%m-%dT%H:%M:%SZ")
            self.updated_at = relativedelta(now, updated_at).hours

            all_issues = repo_json["details"]["all_issues"]["totalCount"]
            close_issues = repo_json["details"]["close_issues"]["totalCount"]
            if all_issues == 0:
                self.issues_rate = 0
            else:
                self.issues_rate = close_issues / all_issues

        if repo_row is not None:
            self.id = repo_row[self.ROW_HEADER[0]]
            self.name_with_owner = repo_row[self.ROW_HEADER[1]]
            self.url = repo_row[self.ROW_HEADER[2]]
            self.created_at = repo_row[self.ROW_HEADER[3]]
            self.updated_at = repo_row[self.ROW_HEADER[4]]
            self.primary_language = repo_row[self.ROW_HEADER[5]]
            self.stargazer_count = repo_row[self.ROW_HEADER[6]]
            self.pull_requests = repo_row[self.ROW_HEADER[7]]
            self.releases = repo_row[self.ROW_HEADER[8]]
            self.issues_rate = repo_row[self.ROW_HEADER[9]]

    def get_string_row(self):
        return [
            self.id,
            self.name_with_owner,
            self.url,
            self.created_at,
            self.updated_at,
            self.primary_language,
            self.stargazer_count,
            self.pull_requests,
            self.releases,
            self.issues_rate,
        ]
