import sys
module_path = '\\'.join(sys.path[0].split('\\')[:-2])
sys.path.append(module_path)

import tempfile
import pytest

from pgbackup import storage

@pytest.fixture()
def infile():
    infile = tempfile.TemporaryFile('r+b')
    infile.write(b"Testing")
    infile.seek(0)
    return infile

def test_storing_file_locally(infile):
    """
    Write content from one file-like to another
    """
    outfile = tempfile.NamedTemporaryFile(delete=False)
    storage.local(infile, outfile)
    with open(outfile.name) as f:
        assert f.read() == "Testing"

def test_storage_file_on_s3(mocker, infile):
    """
    Writes content from one file-like to s3
    """
    client = mocker.Mock()
    mocker.patch.object(client, "upload_fileobj")

    storage.s_3(
        client,
        infile,
        'bucket-name',
        'file-name'
    )

    client.upload_fileobj.assert_called_with(
        infile,
        "bucket-name",
        "file-name"
    )
