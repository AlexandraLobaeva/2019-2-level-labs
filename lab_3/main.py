"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.storage = {}
        self.count_id = 12345

    def put(self, word: str) -> int:
        if word is None:
            return self.storage
        if isinstance(word, int):
            return {}
        if word in self.storage:
            return self.storage
        if word not in self.storage:
            self.storage[word] = self.count_id
            self.count_id += 1
        return self.storage.get(word)

    def get_id_of(self, word: str):
        if word in self.storage:
            return self.storage.get(word)
        if word is None:
            return -1
        if isinstance(word, int):
            return -1
        if word not in self.storage:
            return -1

    def get_original_by(self, id: int) -> str:
        for i in self.storage.items():
            if i[1] == id:
                return i[0]
        if id is None or id not in self.storage:
            return 'UNK'

    def from_corpus(self, corpus: tuple):
        if corpus is None or len(corpus) == 0 or isinstance(corpus, str):
            return {}
        self.storage = []
        for word in corpus:
            if word not in self.storage:
                self.storage.append(word)
        return len(self.storage)


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if sentence is None or len(sentence) == 0 or type(sentence) is not tuple:
            return self.gram_frequencies
        for i in range(len(sentence[:-1])):
            gram = sentence[i:self.size + i]
            if gram not in self.gram_frequencies:
                self.gram_frequencies[gram] = 1
            else:
                self.gram_frequencies[gram] += 1
        if self.gram_frequencies != {}:
            return 'OK'
        else:
            return 'Error'

    def calculate_log_probabilities(self):
        for gram in self.gram_frequencies:
            numerator = 0
            denominator = 0
            for key in self.gram_frequencies:
                if gram == key:
                    numerator += self.gram_frequencies[key]
                if gram[0] == key[0]:
                    denominator += self.gram_frequencies[key]
            probabilities = math.log(numerator / denominator)
            self.gram_log_probabilities[gram] = probabilities
        return self.gram_log_probabilities

    def predict_next_sentence(self, prefix: tuple) -> list:
        if prefix is None or type(prefix) is not tuple or len(prefix) != (self.size - 1):
            return []
        next_sentence = []
        for gram in self.gram_log_probabilities:
            for gram_1 in self.gram_log_probabilities:
                if gram[0] == prefix[0]:
                    if self.gram_log_probabilities[gram] >= self.gram_log_probabilities[gram_1]:
                        if gram[0] not in next_sentence:
                            next_sentence.append(prefix[0])
                            next_sentence.append(gram[1])
                if gram[1] == gram_1[0]:
                    if self.gram_log_probabilities[gram] >= self.gram_log_probabilities[gram_1]:
                        if gram[1] not in next_sentence:
                            next_sentence.append(gram[1])
                if gram_1[1] == gram[0]:
                    if self.gram_log_probabilities[gram] >= self.gram_log_probabilities[gram_1]:
                        if gram[1] not in next_sentence:
                            next_sentence.append(gram[1])
        return next_sentence


word_storage = WordStorage()


def encode(storage_instance, corpus) -> list:
    for sentence in corpus:
        storage = []
        for word in sentence:
            id = word_storage.put(word)
            if id not in storage:
                storage.append(id)
        storage_instance.append(storage)
    return storage_instance


def split_by_sentence(text: str) -> list:
    if text is None:
        return []
    if text == '':
        return []
    if '.' not in text:
        return []
    if not isinstance(text, str):
        text = str(text)
    text = text.lower()
    text = text.replace('\n', '')
    text = text.replace('  ', ' ')
    text = text.replace('!', '.')
    text = text.replace('?', '.')
    new_text = ''
    sentences = []
    corpus = []
    for symbol in text:
        if symbol.isalpha() or symbol == ' ' or symbol == '.':
            new_text += symbol
    new_text = new_text.split('.')
    for sentence in new_text:
        sentence = sentence.split()
        sentences.append(sentence)
    for sentence in sentences:
        if len(sentence) != 0:
            exit = ['<s>']
            for word in sentence:
                exit.append(word)
            exit.append('</s>')
            corpus.append(exit)
    return corpus
   
