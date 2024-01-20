__all__ = ['add_module_to_path', 'cheating_check']
import hashlib
from pathlib import Path
from typing import Iterable, List


class CheatError(Exception):
    pass


HASH_FILE_NAME = ".utils_sha1.txt"


def all_module_files_with_permission(module_path: Path, exclude_patterns: List[str]) -> Iterable[Path]:
    for file_path in module_path.iterdir():
        if any(pattern in file_path.absolute().as_uri() for pattern in exclude_patterns):
            continue
        if not file_path.name.split('.')[-1] == "py":
            continue
        try:
            file_path.read_text()
        except PermissionError:
            continue
        yield file_path


def hash_without_new_lines(path: Path):
    text_without_newlines = path.read_text().replace('\n', 'LINEBREAK')
    hash = hashlib.sha1(text_without_newlines.encode()).digest()
    return hash


def calculate_module_hash(module_path: Path):
    return b''.join(
        hash_without_new_lines(path)
        for path
        in all_module_files_with_permission(module_path, [HASH_FILE_NAME, 'pycache'])
    )


def cheating_check(module_path):
    actual_hash = calculate_module_hash(module_path)
    hash_file_path = module_path / HASH_FILE_NAME
    if not hash_file_path.exists():
        hash_file_path.write_bytes(actual_hash)

    if actual_hash != hash_file_path.read_bytes():
        raise CheatError(
            "The imported utils module has been changed. Are you cheating?")
