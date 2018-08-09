import os
import tempfile


class File:

    def __init__(self, file_path):
        self.file_path = os.path.abspath(file_path)
        self.file_name = os.path.basename(file_path)

    def write(self, *data):
        with open(self.file_path, 'a') as f:
            for d in data:
                f.write(d)

    def read(self):
        with open(self.file_path, 'r') as f:
            return f.read()

    def __add__(self, file):
        import random
        new_file = File(os.path.join(tempfile.gettempdir(),
                                     str(random.getrandbits(32))+'.txt'))
        with open(new_file.file_path, 'w') as f:
            f.write(self.read())
            f.write(file.read())
        return new_file

    def __str__(self):
        return self.file_path

    def __iter__(self):
        return iter(self.read().split(os.linesep))
