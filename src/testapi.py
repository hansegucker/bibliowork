from lib.dataapi import *
from lib.settings import *


def main():
    secret_config = Settings(settings_name="secret_config", file_ending="json")

    api = BookAPI(api_key=secret_config.get("googlebooks_api_key"))
    api.get_book_information(9783404166602)


if __name__ == '__main__':
    main()
