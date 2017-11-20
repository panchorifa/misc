import os
import errno
import shutil
from os.path import isfile, join

# https://en.wikipedia.org/wiki/Composition_over_inheritance
class CommonOps:
    def __init__(self, name, path, type):
        self.name = name
        self.path = path
        self.type = type

    def rename(self, new_name):
        os.rename(self.name, self.new_name)

    def full_path(self):
        return "{}/{}".format(self.path, self.name)

class File:
    def __init__(self, name, path):
        ftype = name.split('.')[1]
        self.ops = CommonOps(name, path, ftype)

    def delete(self):
        os.remove(self.full_path())

    def content(self):
        with open(self.name, 'r') as fin:
            return fin.read()

    def __getattr__(self, attr):
        return getattr(self.ops, attr)


class Dir:
    VISIBLE = 'visible'
    HIDDEN = 'hidden'
    def __init__(self, path, makedir=False):
        path, name = path.rsplit('/', 1)
        dtype = Dir.HIDDEN if name.startswith('.') else Dir.VISIBLE
        self.ops = CommonOps(name, path, dtype)
        if makedir:
            try:
                os.makedirs(path)
            except OSError as exc:
                if exc.errno == errno.EEXIST and os.path.isdir(path):
                    pass
                else:
                    raise

    def files(self):
        return [File(f, self.path) for f in os.listdir(self.path) if isfile(join(self.path, f))]

    def new_file(self, name, text):
        with open(name, 'w') as text_file:
            text_file.write(text)
        return File(name, self.full_path())

    def delete(self):
        shutil.rmtree(self.path)

    def __getattr__(self, attr):
        return getattr(self.ops, attr)
