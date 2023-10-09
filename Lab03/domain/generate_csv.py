from Lab03.domain.repository_crawler_service import RepositoryCrawlerService
from Lab03.domain.repository_model import Repository
from Lab03.domain.repository_csv_service import RepositoryCsvService
from settings import BASE_DIR
import os.path


CURSOR_PATH = f'{BASE_DIR}/Lab03/cursor.txt'


def generate_repository_csv():
    repo_csv = RepositoryCsvService()
    crawler = RepositoryCrawlerService()
    if os.path.exists(CURSOR_PATH):
        with open(CURSOR_PATH, 'r', encoding='utf-8') as f:
            cursor = f.readline()
        repo_csv.start_writer("r")
        count = repo_csv.lines - 1
    else:
        cursor = ""
        repo_csv.remove_file()
        repo_csv.start_writer()
        repo_csv.write_header()
        count = 0

    max_count = 200
    result = crawler.crawl_graphql(cursor)
    while True:
        for repo_json in result["repos"]:
            repo_model = Repository(repo_json)
            repo_csv.write_row(repo_model)
            count += 1
            if count == max_count:
                break
        if count == max_count:
            break
        f = open(CURSOR_PATH, 'w', encoding='utf-8')
        f.write(f'{result["cursor"]}')
        f.flush()
        f.close()
        result = crawler.crawl_graphql(result["cursor"])

    repo_csv.reset_internal()
    os.remove(CURSOR_PATH)


def read_repository_csv():
    repo_csv = RepositoryCsvService()
    repo_csv.start_reader()
    return repo_csv.read_all()


def generate_pull_request_csv():
    crawler = RepositoryCrawlerService()
    repos = read_repository_csv()
    crawler.crawl_rest(repos)
