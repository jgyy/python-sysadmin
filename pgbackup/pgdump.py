# subprocess.Popen(['pg_dump', "postgres://postgres:postgres@127.0.0.1:5432/sample"], stdout=subprocess.PIPE)
import sys
import subprocess

def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError:
        print("Error: pg_dump not found")
        sys.exit(2)
