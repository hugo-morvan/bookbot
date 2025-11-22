def get_num_words(text):
    return len(text.split())


def get_char_stat(text):
    lower_text = text.lower()
    char_dict = {}
    for let in lower_text:
        if let in char_dict:
            char_dict[let] += 1
        else:
            char_dict[let] = 1
    return char_dict


def sort_on(items):
    return items["num"]


def sort_dict(dict):
    dict_list = []
    for key in dict:
        if not key.isalpha():
            continue
        new_dict = {}
        new_dict["name"] = key
        new_dict["num"] = dict[key]
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
