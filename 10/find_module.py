import os
import hashlib
import colors
from virustotal_python import Virustotal
from vt_config import VIRUS_TOTAL_API_KEY

vtotal = Virustotal(VIRUS_TOTAL_API_KEY)

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
        hash = md5_hash.hexdigest()
        colors.print_success(f'[+] File: {filepath}')
        colors.print_header(f'  [~] Size: {os.path.getsize(filepath)} kbs')
        colors.print_header(f'  [~] Hash: {hash}')
        check_hash(hash)



def check_hash(hash):
    try:
        res = vtotal.file_report([hash])
        data = res.get('json_resp')
        if(data.get('response_code') == 0):
            colors.print_header('  [~] No threat found')
            return
        positives = int(data.get("positives"))
        if(positives >= 3):
            colors.print_fail(f'  [!] {positives} Threats found ')
        else:
            colors.print_warning(f'  [!] {positives} Potential threats found')
    except Exception as err:
        colors.print_info("  [!] MAX REQUESTS EXCEEDED")


def main():
    path = input("Path: ") or "./"
    find_files(path)
