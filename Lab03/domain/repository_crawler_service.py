from Lab03.github_api.api_rest import GithubApiRest
from Lab03.github_api.api_graphql import GithubApiGraphql


class RepositoryCrawlerService:

    def __init__(self):
        self.github_api_rest = GithubApiRest()
        self.github_api_graphql = GithubApiGraphql()

    def crawl(self, cursor=""):
        data_json = self.github_api_graphql.top_repos_query_with_prs(cursor)
        if 'error' in data_json:
            raise Exception(f"Unexpected error: {data_json}")
        result_data = data_json['data']['search']['edges']
        cursor = data_json['data']['search']['pageInfo']['endCursor']
        repos = []
        for data in result_data:
            if data['node']['pullRequests']['totalCount'] > 100:
                repos.append(data['node'])

        return {"repos": repos, "cursor": cursor}
