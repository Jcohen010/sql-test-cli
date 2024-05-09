import os
import glob

from sql_test_cli.core.directory_check import ensure_sql_filetype, check_directory


def test_ensure_sql_filetype__true():
    i = 0
    filename = 'test.sql'

    assert ensure_sql_filetype(i, filename) == True

def test_ensure_sql_filetype__false():
    i = 0
    filename = 'test.xml'

    assert ensure_sql_filetype(i, filename) == False

def test_check_directory():
    os.mkdir('testdir')
    os.chdir('testdir')

    open('test1.sql', 'w')
    open('test2.sql', 'w')
    open('test3.xml', 'w')

    file_list = check_directory('.')

    assert file_list == ['test1.sql', 'test2.sql']
    
    os.chdir('..')

    test_files_list = glob.glob('testdir/*')

    for path in test_files_list:
        os.remove(path)

    os.rmdir('testdir')
    

