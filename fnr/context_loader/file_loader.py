class file_loader:
    def __init__(self, f):
        self.file = f
        self.file_format = 'csv'

    def __file_not_found_handler(self):
        print('Err: Input file ({}) not found'.format(self.file) )

    def show(self):
        try:
            with open(self.file) as context_file:
                print(context_file.read())
        except FileNotFoundError:
            self.__file_not_found_handler()

    def get_context_vars(self):
        try:
            with open(self.file) as context_file:
                return {row.split(',')[0]:row.strip().split(',')[1] for row in context_file}
        except FileNotFoundError:
            self.__file_not_found_handler()