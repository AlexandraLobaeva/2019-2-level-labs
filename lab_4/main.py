import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    TEXTS = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in TEXTS:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts_corpus: list) -> list:
    if not isinstance(texts_corpus, list) or not texts_corpus:
        return []
    clean_corpus = []
    for text in texts_corpus:
        if isinstance(text, str):
            text = text.lower()
            clean_text = []
            br = '<br />'
            while br in text:
                text = text.replace(br, ' ')
            one_text = text.split(' ')
            for word in one_text:
                new_word = ''
                for i in word:
                    if i.isalpha():
                        new_word += i
                if new_word != '':
                    clean_text.append(new_word)
            clean_corpus += [clean_text]
    return clean_corpus


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        if self.corpus is not None:
            for text in self.corpus:
                if text is not None and isinstance(text, list):
                    tf_values = {}
                    doc_len = len(text)
                    for word in text:
                        count_prob = 1
                        if isinstance(word, str):
                            if word not in tf_values:
                                tf_values[word] = count_prob / doc_len
                            else:
                                tf_values[word] += count_prob / doc_len
                    self.tf_values.append(tf_values)
        return self.tf_values

    def calculate_idf(self):
        if self.corpus is not None:
            for text in self.corpus:
                if text is not None:
                    unique_words = []
                    for word in text:
                        if word is not None and word not in unique_words and isinstance(word, str):
                            unique_words += [word]
                    count_probs = {}
                    for word in unique_words:
                        count_prob = 0
                        for text in self.corpus:
                            if not text or word in text:
                                count_prob += 1
                        count_probs[word] = count_prob
                        if count_probs.get(word) != 0:
                            corpus_len = len(self.corpus)
                            self.idf_values[word] = math.log(corpus_len / count_probs.get(word))
        return self.idf_values

    def calculate(self):
        if self.idf_values and self.tf_values:
            for text in self.tf_values:
                tf_idf_values = {}
                for word, tf_value in text.items():
                    tf_idf_values[word] = tf_value * self.idf_values.get(word)
                self.tf_idf_values.append(tf_idf_values)
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if not self.tf_idf_values or document_index >= len(self.tf_idf_values):
            return ()
        tf_idf_dict = self.tf_idf_values[document_index][word]
        tf_idf_sort_list = sorted(self.tf_idf_values[document_index], key=lambda x: self.tf_idf_values[document_index][x], reverse=True)
        return tf_idf_dict, tf_idf_sort_list.index(word)



# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
