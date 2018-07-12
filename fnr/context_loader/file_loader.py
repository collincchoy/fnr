class file_loader:
    def __init__(self, f):
        self.file = f

    def __file_not_found_handler__(self):
        print('File not found')

    def show(self):
        with open(self.file) as context_file:
            print(context_file.read())
