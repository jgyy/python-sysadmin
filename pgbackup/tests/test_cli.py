import sys
module_path = '\\'.join(sys.path[0].split('\\')[:-2])
sys.path.append(module_path)

import pytest
from pgbackup import cli

url = "postgres://postgres:postgres@localhost:5432/sample"

@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    """
    Without a specific driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_with_driver(parser):
    """
    The parser will exit if it receives a sriver without a destination.
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'local'])

def test_parser_with_driver_and_destination(parser):
    args = parser.parse_args([url, '--driver', 'local', '/some/path'])

    assert args.driver == 'local'
    assert args.destination == '/some/path'

def test_parser_with_unknown_driver(parser):
    """
    The parser will exit if the driver name is unknown.
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'azure', 'destination'])

def test_parser_with_known_drivers(parser):
    """
    The parser will not exit if the driver name is known
    """
    for driver in ['local', 's3']:
        assert parser.parse_args([url, '--driver', driver, 'destination'])
