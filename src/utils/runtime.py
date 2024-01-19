__all__ = ['add_module_to_path', 'cheating_check']
import sys
import os
import hashlib
from pathlib import Path
from typing import Generator, Iterable, List


def add_module_to_path():

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))


class CheatError(Exception):
    pass


UTILS_HASH_PATH = Path(__file__).parent/".utils_sha1.txt"


def all_module_files_with_permission(exclude_patterns: List[str]) -> Iterable[Path]:
    for file_path in Path(__file__).parent.iterdir():
        if any(pattern in file_path.absolute().as_uri() for pattern in exclude_patterns):
            continue
        try:
            file_path.read_text()
        except PermissionError:
            continue
        yield file_path


def hash_without_new_lines(path: Path):
    text_without_newlines = path.read_text().replace('\n', 'LINEBREAK')
    return hashlib.sha1(text_without_newlines.encode()).digest()


def calculate_module_hash():
    return b''.join(
        hash_without_new_lines(path)
        for path
        in all_module_files_with_permission([UTILS_HASH_PATH.name, 'pycache'])
    )


def cheating_check():
    actual_hash = calculate_module_hash()

    if not UTILS_HASH_PATH.exists():
        UTILS_HASH_PATH.write_bytes(actual_hash)

    if actual_hash != UTILS_HASH_PATH.read_bytes():
        raise CheatError("The imported utils module has been changed. Are you cheating?")
