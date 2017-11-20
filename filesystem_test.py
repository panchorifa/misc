import os
from filesystem import Dir, File

current_dir = os.path.dirname(os.path.realpath(__file__))

dir = Dir('{}/testing'.format(current_dir), True)
file = dir.new_file('simon.txt', 'sometest')

def test_dir():
    assert dir.name == 'testing'
    assert dir.path == current_dir
    assert dir.type == Dir.VISIBLE
    assert dir.full_path() == '{}/testing'.format(current_dir)

def test_file():
    assert file.name == 'simon.txt'
    assert file.path == '{}/testing'.format(current_dir)
    assert file.type == 'txt'
    assert file.full_path() == '{}/testing/simon.txt'.format(current_dir)
