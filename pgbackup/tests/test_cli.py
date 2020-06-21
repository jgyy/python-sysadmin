import pytest
import sys
module_path = '\\'.join(sys.path[0].split('\\')[:-2])
sys.path.append(module_path)

from pgbackup import cli

url = "postgres://postgres:postgres@localhost:5432/sample"

def test_parser_without_driver():
    """
    Without a specific driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args([url])

def test_parser_with_driver():
    """
    The parser will exit if it receives a sriver without a destination.
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'local'])

def test_parser_with_driver_and_destination():
    parser = cli.create_parser()
    args = parser.parse_args([url, '--driver', 'local', '/some/path'])

    assert args.driver == 'local'
    assert args.destination == '/some/path'
