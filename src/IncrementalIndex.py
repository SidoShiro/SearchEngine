import pickle


def load_incr_index(file):
    with open(file, "rb") as f:
        index = pickle.load(f)
    return index


def save_incr_index(index, file):
    """
    Save index on disk
    using pickle python lib
    """
    with open(file, "wb") as f:
        pickle.dump(index, f, pickle.HIGHEST_PROTOCOL)


class Posting:
    def __init__(self, word, urls):
        """
        word - string
        urls - list of url
        """
        self.word = word
        self.urls = urls

    pass


def make_posting_list(TokeneizedDocs):
    """
    TokeneizedDocs - list of TokenizedDoc
    """
    done_words = []
    postingList = []

    words = []
    for tokD in TokeneizedDocs:
        words += tokD.words

    print("Number of words ", len(words))
    for w in words:
        if w in done_words:
            continue

        done_words.append(w)
        urls = []
        for d in TokeneizedDocs:
            if w in d.words:
                urls.append(d.url)
        postingList.append(Posting(w, urls))

    return postingList


class Generation:
    def __init__(self, gen_id, wordToDocIds, didToMetaData):
        self.gen_id = gen_id
        self.wordToDocIds = wordToDocIds
        # Bonus 1 : Meta Datas
        self.didToMetaData = didToMetaData


class IncrementalIndex:
    def __init__(self):
        self.ids = 0
        self.urlToDocId = {}
        self.idToDocUrl = {}
        self.docIdToGeneration = {}  # key (gen) = [doc id, ...]
        self.generations = []
        # Bonus 2 : Suppr vector
        self.suppressions = []

    def get_doc(self, doclist, url):
        for i in doclist:
            if i.url == url:
                return i
        return None

    def rm_doc(self, url):
        """
        Remove a document
        url - document url to remove
        """
        url_id = self.urlToDocId[url]
        if not (url_id in self.suppressions):
            self.suppressions.append(url_id)
        # print(self.suppressions)

    def build_gen(self, Postings, doclist):
        """
        Build Index from list of Posting
        """
        gen_id = len(self.generations)
        wordToDocIds = {}
        docIdToMetaData = {}  # Dict of MetaDatas
        for i in Postings:
            u_list = []
            for j in i.urls:
                if not (j in self.urlToDocId):
                    self.urlToDocId[j] = self.ids
                    self.idToDocUrl[self.ids] = j
                    self.docIdToGeneration[self.ids] = gen_id
                    u_list.append(self.ids)
                    x = self.get_doc(doclist, j)
                    if x:
                        docIdToMetaData[self.ids] = x.metadata
                    else:
                        docIdToMetaData[self.ids] = None
                    self.ids += 1
                else:
                    u_list.append(self.urlToDocId[j])
            wordToDocIds[i.word] = u_list
        self.generations.append(Generation(gen_id, wordToDocIds, docIdToMetaData))


"""
Create Index
"""
# index = IncrementalIndex()

# Doc = fetch(path_to_files)

# tokdoc = make_tokens(Doc, Processors)

# postingList = make_posting_list(tokdoc)

# index.build_gen(postingList)
