#以下代码属于二次开发

import hashlib
import os

def ifright(file_path: str) -> str:
    if not os.path.isfile(file_path):
        return 'error'


def file_hash(file_path: str, hash_method) -> str:
    h = hash_method()
    with open(file_path, 'rb') as f:
        while True:
            b = f.read(8192)
            if not b:
                break	
            h.update(b)
    return h.hexdigest()

def file_md5(file_path: str) -> str:
    return file_hash(file_path, hashlib.md5)

def file_sha256(file_path: str) -> str:
    return file_hash(file_path, hashlib.sha256)

def file_sha512(file_path: str) -> str:
    return file_hash(file_path, hashlib.sha512)

def file_sha1(file_path: str) -> str:
    return file_hash(file_path, hashlib.sha1)

