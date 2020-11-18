import os
import hashlib
import colors

def find_files(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            filepath = os.path.join(root, name)
            hash_file(filepath)


def hash_file(filepath):
    md5_hash = hashlib.md5()
    with open(filepath, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b''):
            md5_hash.update(byte_block)
        colors.print_success(f'[+] File: {filepath}')
        colors.print_header(f'  [~] Hash: {md5_hash.hexdigest()}')


def main():
    path = input("Path: ") or "./"
    find_files(path)
