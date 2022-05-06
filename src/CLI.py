from Document import *
from IncrementalIndex import *
from IncrementalIndexSearcher import *
from Processors import *
import os.path

version = "v1.0"


def index_paths(l, core_index):
    for path in l:
        docs = fetch(path)
        tokens = make_tokens(docs, Processors)

        # for i in tokens:
        #     print(i.words)

        posting_list = make_posting_list(tokens)
        core_index.build_gen(posting_list, docs)


def remove_in_index_doc(doc, core_index):
    core_index.rm_doc(doc)


def error_no_argument(x):
    if len(x) == 1:
        print("Error: this command require arguments")
        return False
    return True


# Old config
# test_path = ["test"]
# core_index = IncrementalIndex()
# index_paths(test_path, core_index)

core_index = IncrementalIndex()
core_index_name = "undefined"
searcher = IncrementalIndexSearcher(core_index)
index_changed = False

print(" * SE - " + version + " * ")
# CLI
while True:
    searcher.setIndex(core_index, core_index_name)
    s = input("> ")
    x = s.split()

    if len(x) == 0:
        continue

    if "search" == x[0] and error_no_argument(x):
        res = searcher.searchAllOf(x[1:])
        print(res)

    if "search_or" == x[0] and error_no_argument(x):
        res = searcher.searchOneOf(x[1:])
        print(res)

    if "add" == x[0] and error_no_argument(x):
        doc_paths = x[1:]
        index_paths(doc_paths, core_index)
        index_changed = True

    if "remove" == x[0] and error_no_argument(x):
        doc_paths = x[1:]
        for doc in doc_paths:
            remove_in_index_doc(doc, core_index)

    if "load" == x[0] and error_no_argument(x):
        if os.path.exists(x[1]):
            core_index = load_incr_index(x[1])
            core_index_name = x[1]
            print("Index loaded from file " + x[1])
        else:
            print("Error: Try to load index from file " + x[1] + ", but " + x[1] + " doesn't exist!")

    if "save" == x[0] and error_no_argument(x):
        save_incr_index(core_index, x[1])
        print("Index saved in file " + x[1])

    if "new" == x[0]:
        if index_changed:
            execute_new = False
            while True:
                print("Current index has unsaved changed do you want to continue ? Y/n")
                s = input("Y or n > ")
                x1 = s.split()
                if len(x1) > 0 and x1[0] != 'Y':
                    print("(don't execute new command, index " + core_index_name + " still in use)")
                    execute_new = False
                    break
                elif len(x1) > 0 and x1[0] == 'Y':
                    execute_new = True
                    break
            if not execute_new:
                continue
        index_changed = False
        # Create Empty index
        core_index = IncrementalIndex()
        if len(x) >= 2:
            core_index_name = x[1]
        else:
            core_index_name = "undefined"

    if "exit" == x[0] or "quit" == x[0]:
        print("Stop search engine...")
        break

    if "version" == x[0]:
        print("Search Engine " + version + " -- SidoShiro on GitHub (2019)\n\n")

    if "status" == x[0]:
        print("Current index: " + searcher.get_index_name())
        if searcher.getIndex():
            print("number of indexed docs: " + str(len(searcher.getIndex().docIdToGeneration)))
        if searcher.getIndex() and searcher.getIndex().generations and len(searcher.getIndex().generations) > 0:
            print("number of indexed words (in last generation): " +
                  str(len(searcher.getIndex().generations[-1].wordToDocIds)))
        if searcher.getIndex() and searcher.getIndex().generations:
            print("number of generations: " + str(len(searcher.getIndex().generations)))

    if "help" == x[0] or "h" == x[0] or "?" == x[0]:
        print(
            "Search Engine Help :\n"
            "\n"
            "  Commands:\n"
            "  ---------\n"
            "search [words]     : Return result of the docs were the words are present (AND operation by default)\n"
            "search_or [words]  : Make search operation, but any document with at least one of words (OR operation)\n"
            "add [paths]        : Index all files that are in the paths, create a new generation\n"
            "remove [documents] : Remove documents, must be full path, update in a new generation\n"
            "status             : Give information about the loaded index\n"
            "load [index]       : Load an index file\n"
            "save [index]       : Save current index (+ generation) into index\n"
            "new (index_name)   : Create a new empty index, use the 'add' command to index files, optional index name\n"
            "exit|quit          : Stop Engine\n"
            "version            : Show version\n"
            "help|h|?           : Show help\n"
        )
