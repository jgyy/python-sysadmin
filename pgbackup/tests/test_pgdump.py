import sys
module_path = '\\'.join(sys.path[0].split('\\')[:-2])
sys.path.append(module_path)

import pytest
import subprocess

from pgbackup import pgdump

url = "postgres://postgres:postgres@127.0.0.1:5432/sample"

def test_dump_call_pg_dump(mocker):
    """
    Utilize pg_dump to interact with Database
    """
    proc = mocker.Mock()
    mocker.patch('subprocess.Popen', return_value=proc)
    assert pgdump.dump(url) == proc
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)

def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns a reasonable error if pg_dump isn't installed.
    """
    mocker.patch('subprocess.Popen', side_effect=OSError("no such file"))
    with pytest.raises(SystemExit):
        pgdump.dump(url)
