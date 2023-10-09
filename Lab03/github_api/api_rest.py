from settings import env_config
import requests
import json


class GithubApiRest:
    URL = "https://api.github.com/repos"
    HEADERS = {
        "Authorization": "Bearer " + env_config('TOKEN'),
        "X-GitHub-Api-Version": "2022-11-28"
    }

    def repos_pulls(self, name_with_owner, page=1):
        url = f"{self.URL}/{name_with_owner}/pulls?state=closed&sort=created&per_page=20&page={page}"
        request = requests.get(url, headers=self.HEADERS)
        if request.status_code == 200:
            try:
                response_json = request.json()
            except json.JSONDecodeError:
                response_json = {
                    'error': 'JSON Error',
                    'info': request.text
                }
            return response_json
        else:
            raise Exception(f"Unexpected status code returned: {request.status_code}. With response {request.json()}")

    def pulls_review_comments(self, name_with_owner, number):
        url = f"{self.URL}/{name_with_owner}/pulls/{number}/comments"
        request = requests.get(url, headers=self.HEADERS)
        if request.status_code == 200:
            try:
                response_json = request.json()
            except json.JSONDecodeError:
                response_json = {
                    'error': 'JSON Error',
                    'info': request.text
                }
            return response_json
        else:
            raise Exception(f"Unexpected status code returned: {request.status_code}. With response {request.json()}")
