from Lab01.domain.repository_crawler_service import RepositoryCrawlerService
from Lab01.domain.repository_model import Repository
from Lab01.domain.repository_csv_service import RepositoryCsvService


def generate_repository_csv():
    repo_csv = RepositoryCsvService()
    repo_csv.remove_file()
    repo_csv.start_writer()
    repo_csv.write_header()

    crawler = RepositoryCrawlerService()

    result = crawler.crawl()
    for page in range(1, 11):
        for repo_json in result["repos"]:
            repo_model = Repository(repo_json)
            repo_csv.write_row(repo_model)
        result = crawler.crawl(result["cursor"])

    repo_csv.reset_internal()


def read_repository_csv():
    repo_csv = RepositoryCsvService()
    repo_csv.start_reader()
    return repo_csv.read_all()
