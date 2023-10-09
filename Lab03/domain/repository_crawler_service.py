from Lab03.github_api.api_graphql import GithubApiGraphql
from Lab03.github_api.api_rest import GithubApiRest
from datetime import datetime, timedelta


class RepositoryCrawlerService:

    def __init__(self):
        self.github_api_rest = GithubApiRest()
        self.github_api_graphql = GithubApiGraphql()

    def crawl_graphql(self, cursor=""):
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

    def crawl_rest(self, repos):
        page = 1
        for repo in repos:
            data_pulls_json = self.github_api_rest.repos_pulls(repo.name_with_owner, page)
            for data in data_pulls_json:
                data_reviews_json = self.github_api_rest.pulls_review_comments(repo.name_with_owner, data['number'])
                reviews_count = len(data_reviews_json)
                if reviews_count > 0:
                    created_at = datetime.strptime(data['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                    closed_at = datetime.strptime(data['closed_at'], '%Y-%m-%dT%H:%M:%SZ')
                    time_diff = closed_at - created_at
                    if time_diff > timedelta(hours=1):
                        size = data['size']
                        body_length = len(data['body'])
                        description_length = len(data['description'])
                        users = []
                        for review in data_reviews_json:
                            if review['user']['id'] not in users:
                                users.append(review['user']['id'])
                        users_count = len(users)
                        interaction = {
                            'participantes': users_count,
                            'comentários': reviews_count
                        }
                        result = {
                            'Tamanho': size,
                            'Tempo de Análise': time_diff,
                            'Descrição': body_length,
                            'Descrição 2': description_length,
                            'Interações': interaction,
                        }
                        print(result)
            page += 1
