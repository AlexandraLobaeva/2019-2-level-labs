"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
def calculate_frequences(text):
    if text == '' or text is None:
        return {}
    text = str(text)
    text = text.lower()
    splitting = text.split(' ')
    result = []
    prohibited_marks = ['@', '\n', '&', "-", ".", ',', "'", '$', ')', '(', '%', ':', '', '*', '~', '\n\n', '^', '"']
    for word in splitting:
        if not word.isdigit() and word not in prohibited_marks:
            clear_txt = ''
            for i in word:
                if i not in prohibited_marks:
                    clear_txt += i
            if clear_txt is not ' ':
                result.append(clear_txt)
    text_dict = {}
    for word in result:
        if word not in text_dict:
            text_dict[word] = 1
        elif word in text_dict:
            text_dict[word] += 1
    return text_dict
    pass


def filter_stop_words(frequencies, stop_words):
    if frequencies is None:
        return {}
    if stop_words is None:
        return frequencies
    this_dict_copy = frequencies.copy()
    for k in frequencies:
        if type(k) == int:
            del this_dict_copy[k]
        for i in stop_words:
            if k == i:
                del this_dict_copy[k]
    return this_dict_copy
    pass


def get_top_n(frequencies, top_n):
    import operator
    top = sorted(frequencies.items(), key=operator.itemgetter(1))
    top = top[::-1]
    n_top = top[:top_n]
    tuple_key = []
    for k in n_top:
        tuple_key.append(k[0])
    tuple_key = tuple(tuple_key)
    if top_n < 0:
        return ()
    return tuple_key
    pass
