
from pathlib import Path


def _valid_path(path):
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found:{file_path}")
    return file_path

def parse_resume(file_path):
    #validate path
    file_path = _valid_path(file_path)
    
    #open and read
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    #return text
    return text

def parse_jd(file_path):
    file_path = _valid_path(file_path)

    with open(file_path, 'r', encoding='utf-8') as f:
        text =f.read()

    return text