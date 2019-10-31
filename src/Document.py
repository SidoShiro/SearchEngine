from os import listdir, stat
from os.path import isfile, isdir, join, exists


class Doc:
    def __init__(self, url, text, metadata={}):
        self.text = text  # Raw strnig of the whole text
        self.url = url
        self.metadata = metadata

    pass


def fetch(path, recursive=True):
    if not exists(path):
        print("Error: " + path + " doesn't exist.")
        return False

    doc_list = []

    # handle case that path is file
    if isfile(path):
        f = open(path, errors="ignore")
        try:
            c = f.read()
            metadata = {}
            metadata["name"] = path
            metadata["file"] = path
            metadata["date"] = stat(path).st_mtime
            doc_list.append(Doc(path, c, metadata))
        except Exception:
            pass
        f.close()
        return doc_list

    # General case, directory
    files = [f for f in listdir(path) if isfile(join(path, f))]
    dirs = [d for d in listdir(path) if isdir(join(path, d))]

    for f_name in files:
        f = open(path + "/" + f_name, "r", errors="ignore")
        try:
            c = f.read()
            metadata = {}
            metadata["name"] = f_name
            metadata["file"] = f_name
            metadata["date"] = stat(path + "/" + f_name).st_mtime
            doc_list.append(Doc(path + "/" + f_name, c, metadata))
        except Exception:
            pass
        f.close()

    if recursive:
        for d in dirs:
            doc_list += fetch(join(path, d), recursive=recursive)

    return doc_list


class FoundDocument:
    def __init__(self, url, metaDatas):
        self.url = url
        self.metaDatas = metaDatas


