class BookAPI():

    def __init__(self, api_key):
        from apiclient.discovery import build
        self.api = build('books', 'v1', developerKey=api_key)
        self.collection = self.api.volumes()

    def get_book_information(self, isbn):
        request = self.collection.list(q='isbn:' + str(isbn))
        response = request.execute()
        self.json_data = response
        self.print_data()

    def print_data(self):
        item = self.json_data['items'][0]['volumeInfo']
        print(self.json_data['items'][0])
        print('#########')
        print('# DATEN #')
        print('#########')
        print('Titel: ' + item['title'])
        print('Autor(en): ' + item['authors'][0])
