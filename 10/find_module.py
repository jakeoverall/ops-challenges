import os
import fnmatch


def find_files(filename, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, filename):
                match = os.path.join(root, name)
                print(match)
                result.append(match)
    return result


def main():
    filename = input("Filename: ")
    path = input("Path: ") or "."
    find_files(filename, path)
