from settings import env_config
import requests
import json


class GithubApiRest:
    URL = "https://api.github.com/repos"
    HEADERS = {
        "Authorization": "Bearer " + env_config('TOKEN'),
        "X-GitHub-Api-Version": "2022-11-28"
    }

    def pull_requests(self, name_with_owner):
        page = 1
        prs = []

        while True:
            url = f"{self.URL}/{name_with_owner}/pulls?state=closed&per_page=100&page={page}"
            request = requests.get(url, headers=self.HEADERS)
            if request.status_code == 200:
                try:
                    response_json = request.json()
                    prs = prs + response_json
                    if 'next' in request.links:
                        page = page + 1
                    else:
                        return prs
                except json.JSONDecodeError:
                    response_json = {
                        'error': 'JSON Error',
                        'info': request.text
                    }
                    return response_json
            else:
                raise Exception(f"Unexpected status code returned: {request.status_code}. With response {request.json()}")

    def pulls_reviews(self, name_with_owner, number):
        url = f"{self.URL}/{name_with_owner}/pulls/{number}/reviews"
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

    def pulls_comments(self, name_with_owner, number):
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

    def pulls_review_files(self, name_with_owner, number):
        url = f"{self.URL}/{name_with_owner}/pulls/{number}/files"
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


# Merged or Closed
# At least 1 revision
# At least 1 hour revision time