from ast import parse
import pytest
import os

from sql_test_cli.core.config import config_check, parse_config_yaml, locate_root_dir

def test_conf_check():
    uri = None
    target_dir = None
    filepath = None

    with pytest.raises(SystemExit):
        config_check(uri, target_dir, filepath)


def test_parse_config_yaml__invalid_yaml():
    with open('test.yml', 'w') as f:
        f.write("app_env: ''\nlog_level: WARN\ntarget_dir: ''\nuri: '")

    with pytest.raises(Exception):
        parse_config_yaml('test.yml')

    os.remove('test.yml')

def test_parse_config_yaml__values():
    with open('test.yml', 'w') as f:
        f.write("app_env: 'dev'\nlog_level: WARN\ntarget_dir: 'test'\nuri: 'sqlite:////C:/Users/Giang/PyCharmProjects/FlaskWebBlog/FlaskWebBlog/site.db'")

    app_env, uri, target_dir, log_level = parse_config_yaml('test.yml')

    assert app_env == 'dev'
    assert uri == 'sqlite:////C:/Users/Giang/PyCharmProjects/FlaskWebBlog/FlaskWebBlog/site.db'
    assert target_dir == 'test'
    assert log_level == 'WARN'

    os.remove('test.yml')    

def test_locate_root_dir(): 
    os.mkdir('./test')
    os.mkdir('./test/folder')
    os.mkdir('./test/folder/path')
    open('./test/folder/sql-test-cli.yaml', 'w')
    os.chdir('./test/folder/path')

    root = locate_root_dir()

    os.chdir('../../../') 
    os.remove('./test/folder/sql-test-cli.yaml')
    os.rmdir('./test/folder/path')
    os.rmdir('./test/folder')
    os.rmdir('./test')
    print(root)

    assert root[-12:] == "\\test\\folder"







