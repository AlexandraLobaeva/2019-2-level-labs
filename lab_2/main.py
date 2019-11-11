"""
Labour work #2. Levenshtein distance.
"""


import csv


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    if num_rows is None or num_cols is None:
        return []
    if isinstance(num_rows, str):
        return []
    if isinstance(num_cols, str):
        return []
    if num_rows == [] or num_cols == []:
        return []
    edit_matrix = [[0 for col in range(num_cols)] for row in range(num_rows)]
    return edit_matrix


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    if not edit_matrix:
        return []
    if [] in edit_matrix:
        return edit_matrix
    if isinstance(remove_weight, str):
        return edit_matrix
    if isinstance(add_weight, str):
        return edit_matrix
    if remove_weight == [] or add_weight == []:
        return edit_matrix
    if remove_weight is None or add_weight is None:
        return edit_matrix
    count_col = 0
    for col in edit_matrix:
        col[0] = count_col
        count_col += remove_weight
    count_row = 0
    row = edit_matrix[0]
    for index, item in enumerate(row):
        if item == 0:
            row[index] = count_row
        count_row += add_weight
    return edit_matrix


def minimum_value(numbers: tuple) -> int:
    return min(numbers)


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    if original_word is None or target_word == '':
        return edit_matrix
    if substitute_weight == [] or remove_weight is None or isinstance(add_weight, str):
        return edit_matrix
    if [] in edit_matrix:
        return []
    if not edit_matrix:
        return edit_matrix
    for o in enumerate(original_word, 1):
        for t in enumerate(target_word, 1):
            i, j = o[0], t[0]
            if o[1] == t[1]:
                add, remove, substitute = edit_matrix[i][j - 1] + add_weight, edit_matrix[i - 1][j] + remove_weight, edit_matrix[i - 1][j - 1] + 0
            else:
                add, remove, substitute = edit_matrix[i][j - 1] + add_weight, edit_matrix[i - 1][j] + remove_weight, edit_matrix[i - 1][j - 1] + substitute_weight
            (numbers) = (add, remove, substitute)
            edit_matrix[i][j] = minimum_value(numbers)
    return edit_matrix


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    if isinstance(original_word, int) or target_word == []:
        return -1
    if isinstance(add_weight, str) or remove_weight == [] or substitute_weight is None:
        return -1
    num_rows = len(original_word) + 1
    num_cols = len(target_word) + 1
    edit_matrix = generate_edit_matrix(num_rows, num_cols)
    initialized_matrix = initialize_edit_matrix(edit_matrix, add_weight, remove_weight)
    filled_matrix = fill_edit_matrix(initialized_matrix, add_weight, remove_weight, substitute_weight, original_word, target_word)
    return filled_matrix[-1][-1]


def save_to_csv(edit_matrix: tuple, path_to_file: str) -> None:
    with open(path_to_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(edit_matrix)
    return None


def load_from_csv(path_to_file: str) -> list:
    with open(path_to_file, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    return list(row)

