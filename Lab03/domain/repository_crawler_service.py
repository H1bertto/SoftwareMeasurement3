from Lab01.external.github_api import GithubApi


class RepositoryCrawlerService:

    def __init__(self):
        self.github_api = GithubApi()

    def crawl(self, cursor=""):
        data_json = self.github_api.top_repos_query(cursor)
        if 'error' in data_json:
            raise Exception(f"Unexpected error: {data_json}")
        data = data_json['data']['search']['edges']
        cursor = data_json['data']['search']['pageInfo']['endCursor']
        repos = []

        count = 0
        for node in data:
            repo = node['node']
            search_id = repo['nameWithOwner']
            print(f"{count}. Getting details for {search_id}")
            details = self.github_api.repo_details_query(search_id)['data']['search']['edges'][0]['node']
            if 'error' in details:
                raise Exception(f"Unexpected error: {data_json}")
            repo['details'] = details
            repos.append(repo)
            count += 1

        return {"repos": repos, "cursor": cursor}
