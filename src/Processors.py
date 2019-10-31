class LowerProcessor:
    def __init__(self):
        pass

    def process(word):
        """
        word      - string
        return    - processed string
        """
        proc_word = word.lower()
        return proc_word


class AccentProcessor:
    def __init__(self):
        pass

    def process(word):
        """
        word      - string
        return    - processed string
        """
        proc_word = word.replace("'", " ")
        proc_word = proc_word.replace("`", " ")
        proc_word = proc_word.replace("\"", "")
        return proc_word


class PunctationProcessor:
    def __init__(self):
        pass

    def process(word):
        """
        word      - string
        return    - processed string
        """
        proc_word = word.replace(".", " ")
        proc_word = proc_word.replace(",", " ")
        proc_word = proc_word.replace(";", "")
        proc_word = proc_word.replace(":", "")
        proc_word = proc_word.replace("!", "")
        proc_word = proc_word.replace("?", "")
        proc_word = proc_word.replace("\n", "  ")
        return proc_word


class SpecialProcessor:
    def __init__(self):
        pass

    def process(word):
        """
        word      - string
        return    - processed string
        """
        proc_word = word.replace("(", "")
        proc_word = proc_word.replace("#", " ")
        proc_word = proc_word.replace("-", " ")
        proc_word = proc_word.replace("_", " ")
        proc_word = proc_word.replace("=", " ")
        proc_word = proc_word.replace("*", " ")
        proc_word = proc_word.replace("<", "")
        proc_word = proc_word.replace(">", "")
        proc_word = proc_word.replace(")", "")
        proc_word = proc_word.replace("/", "")
        proc_word = proc_word.replace("\\", "")
        proc_word = proc_word.replace("[", "")
        proc_word = proc_word.replace("^", "")
        proc_word = proc_word.replace("]", "")
        proc_word = proc_word.replace("", "")
        proc_word = proc_word.replace(" ", "")
        proc_word = proc_word.replace("  ", "")
        return proc_word


class TokenizedDoc:
    def __init__(self, words, url):
        self.words = words  # list of strings (list of words)
        self.url = url

    pass


def make_tokens(docs, processorsList):
    """
    docs           - list of Docs
    processorsList - list of Processors like TextProcessor
    return         - list of TokenizedDoc
    """

    # Check if error argument
    if type(docs) is not list:
        return []

    tokdocs = []
    for d in docs:
        tokens = d.text.split(" ")  # Split and tokenzie on ' ', return list of words
        # Process
        words = []
        for w in tokens:
            w = w.strip()
            for p in processorsList:
                w = p.process(w)
            w_r = w.split()
            for w in w_r:
                if w != '' and w != ' ':
                    words.append(w)
        tokdocs.append(TokenizedDoc(words, d.url))
    return tokdocs


Processors = [PunctationProcessor, SpecialProcessor, AccentProcessor, LowerProcessor]
