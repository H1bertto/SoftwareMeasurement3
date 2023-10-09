from settings import env_config
import requests
import json


class GithubApiRest:
    URL = "https://api.github.com"
    HEADERS = {"Authorization": "Bearer " + env_config('TOKEN')}

    def most_popular_repos(self, page=1):
        # url_query = f"{self.URL}/search/repositories?q=stars:>0&sort=stars&order=desc&per_page=25&page={page}"
        # url_query = f"{self.URL}/search/repositories?q=stars:>0+is:public+is:popular+pr:>100&sort=stars&order=desc&per_page=25&page={page}"
        url_query = f"{self.URL}/search/repositories?q=stars:>0+pull-request:>=100&sort=stars&order=desc&per_page=25&page={page}"
        request = requests.get(url_query, headers=self.HEADERS)
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
