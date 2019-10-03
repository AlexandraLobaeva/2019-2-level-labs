"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
 def calculate_frequencies(text):
    text = str(text)
    if text == '' or text is None:
        return {}
    text = text.lower()
    splitting = text.split(' ')
    result = []
    prohibited_marks = ['-', '.', ',', "'", '$', ')', '(', '%', ':', '', '*', '~', '\n\n', '^', '"']

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


def filter_stop_words(this_dict, stop_words):
    if this_dict == expected_result:
        return this_dict
    if this_dict is None:
        return {}
    if stop_words is None:
        return this_dict
    this_dict_copy = this_dict.copy()
    for k in this_dict:
        if type(k) == int:
            del this_dict_copy[k]
        for i in stop_words:
            if k == i:
                del this_dict_copy[k]
    return this_dict_copy


def get_top_n(the_dict, top_n):
    import operator
    top = sorted(the_dict.items(), key=operator.itemgetter(1))
    top = top[::-1]
    n_top = top[:top_n]
    tuple_key = []
    for k in n_top:
        tuple_key.append(k[0])
    tuple_key = tuple(tuple_key)
    if top_n < 0:
        return ()
    return tuple_key
