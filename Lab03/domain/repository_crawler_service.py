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
            prs_json = self.github_api_rest.pull_requests(repo.name_with_owner)
            for pr in prs_json:
                user_reviews_json = self.github_api_rest.pulls_reviews(repo.name_with_owner, pr['number'])
                user_comments_json = self.github_api_rest.pulls_comments(repo.name_with_owner, pr['number'])
                files_json = self.github_api_rest.pulls_review_files(repo.name_with_owner, pr['number'])

                lines_changed = 0
                files_changed = len(files_json)
                for file in files_json:
                    lines_changed += file["changes"]

                reviews_count = len(user_reviews_json)
                if reviews_count > 0:

                    created_at = datetime.strptime(pr['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                    time_diff = None

                    if 'merged_at' in pr:
                        merged_at = datetime.strptime(pr['merged_at'], '%Y-%m-%dT%H:%M:%SZ')
                        time_diff = merged_at - created_at
                    else:
                        closed_at = datetime.strptime(pr['closed_at'], '%Y-%m-%dT%H:%M:%SZ')
                        time_diff = closed_at - created_at

                    if time_diff > timedelta(hours=1):

                        body_length = len(pr['body']) + len(pr['title'])
                        users = []
                        for review in user_reviews_json:
                            if review['user']['id'] not in users:
                                users.append(review['user']['id'])
                        for comment in user_comments_json:
                            if comment['user']['id'] not in users:
                                users.append(comment['user']['id'])

                        users_count = len(users)
                        interaction = {
                            'participantes': users_count,
                            'comentários': reviews_count
                        }
                        result = {
                            'Quantidade Arquivos': files_changed,
                            'Quantidade de Linhas': lines_changed,
                            'Tempo de Análise': time_diff,
                            'Descrição': body_length,
                            'Interações': interaction,
                        }
                        print(result)
            page += 1