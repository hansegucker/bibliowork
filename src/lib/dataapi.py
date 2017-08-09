class BookAPI():

    from apiclient.discovery import build

    def __init__(self, api_key):
        self.api = self.build('books', 'v1', developerKey=api_key)
        self.collection = self.api.volumes()

    def get_book_information(self, isbn):
        request = self.collection.list('isbn:' + str(isbn))
        response = request.execute()
        self.json_data = response
        self.print_data()

    def print_data(self):
        print(self.json_data)
