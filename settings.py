from decouple import Config, RepositoryEnv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DOTENV_FILE = f'{BASE_DIR}/lab.env'
env_config = Config(RepositoryEnv(DOTENV_FILE))
