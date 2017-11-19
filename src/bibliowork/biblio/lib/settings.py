class Settings():

    def __init__(self, settings_name, file_ending='json'):
        file_name = settings_name + '.' + file_ending
        self.data = self.read_config(file_name)

    def read_config(self, file_name):
        import json

        with open(file_name, 'r') as f:
            data = json.load(f)

        return data

    def get(self, key):
        return self.data.get(key)
