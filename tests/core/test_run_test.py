import pandas as pd 
import os

from sql_test_cli.core.utils import clean_run_dir
from sql_test_cli.core.run_test import read_sql_file, run_sql_test, create_failure_file, handle_test_result

def test_read_sql_file():
    with open('test.sql', 'w') as f:
        f.write(
            '''
                select *\n
                from test\n
                where column = 1
            '''
        )

    test_sql, test_file_path = read_sql_file('test.sql')

    os.remove('test.sql')   

    assert test_sql == '''
                select *\n
                from test\n
                where column = 1
            '''

    assert test_file_path == 'test.sql'

def test_run_sql_tests():
    pass

def test_create_failure_file():
    pass

def test_handle_test_result__pass(capsys):
    empty_dict = {}
    empty_df = pd.DataFrame(empty_dict)

    handle_test_result(test_result_df=empty_df, test_duration=0.6, test_filename='test.sql', test_file_path='./test.sql')
    captured_output = capsys.readouterr().out.strip()

    assert captured_output == 'PASS [0.6 second(s)]'
    
    
def test_handle_test_result__fail(capsys):
    clean_run_dir()

    dict = {'a' : [1,2,3], 'b' : [4,5,6]}
    df = pd.DataFrame(dict)
    
    handle_test_result(test_result_df=df, test_duration=0.6, test_filename='test.sql', test_file_path='./test.sql')
    captured_output = capsys.readouterr().out.strip()

    assert 'FAIL' in captured_output

    failure_files = clean_run_dir()

    assert failure_files != []