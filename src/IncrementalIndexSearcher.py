import pickle
from Document import *


class IncrementalIndexSearcher:
    def __init__(self, index_incr=None):
        if index_incr is None:
            print("Warning: No index linked to searcher!")
        else:
            self.index = index_incr

    def load(self, path):
        with open(path + "/" + "index_incr.bin", "rb") as f:
            self.index = pickle.load(f)

    def getIndex(self):
        return self.index

    def setIndex(self, index):
        self.index = index

    def id_to_url(self, id_l):
        res = []
        for i in id_l:
            res.append(self.index.idToDocUrl[i])
        return res

    # Bonus 1 Search Metadatas, for 1 word search
    def search_meta(self, word):
        res = []
        res_ids = self.search_ids(word)
        for i in res_ids:
            gen_id = self.index.docIdToGeneration[i]  # Give gen of this doc id
            gen = self.index.generations[gen_id]
            url = self.index.idToDocUrl[i]
            metas = gen.didToMetaData[i]
            res.append(FoundDocument(url, metas))
        return res

    def search(self, word):
        res_id = self.search_ids(word)
        res_urls = self.id_to_url(res_id)
        return res_urls

    def search_ids(self, word):
        """
        Search word, return urls for this word
        word      - string
        """
        gs = self.index.generations
        res = []
        gl = len(self.index.generations)
        current_urls = []
        for g in reversed(gs):  # Get last first
            if not (word in g.wordToDocIds):
                continue
            preserved_urls = []
            urls_ids = list.copy(g.wordToDocIds[word])
            urls = []
            for u in urls_ids:
                urls.append(self.index.idToDocUrl[u])
            for u in urls:
                if not (u in current_urls):
                    preserved_urls.append(u)
                    current_urls.append(u)
            urls_ids = []
            for u in preserved_urls:
                # Bonus 2 :  Handle supp
                url_id = self.index.urlToDocId[u]
                if url_id in self.index.suppressions:
                    print("sup found", self.index.suppressions)
                    continue
                urls_ids.append(url_id)
            res = res + urls_ids
        return res

    def searchAllOf(self, words):
        """
        AND oper
        words - list of words
        """
        and_urls = []
        first = True
        for w in words:
            if first:
                and_urls = self.search_ids(w)
                first = False
            else:
                and_urls = list(set(and_urls) & set(self.search_ids(w)))
        res_urls = self.id_to_url(and_urls)
        return res_urls

    def searchOneOf(self, words):
        """
        OR oper
        """
        or_urls = []
        for w in words:
            or_urls = list(set(or_urls) | set(self.search_ids(w)))
        res_urls = self.id_to_url(or_urls)
        return res_urls
