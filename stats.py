def get_num_words(filename):
    with open(filename, 'r') as file:
       text = file.read()
    num_words = len(text.split())
    return f"Found {num_words} total words"

def get_character_count(filename):
    char_count = []
    with open(filename, 'r') as file:
        text = file.read()
    for char in text:
        lchar = char.lower()
        if lchar.isalpha():
            found = False
            for item in char_count:
                if item['char'] == lchar:
                    item['count'] += 1
                    found = True
                    break
            if not found:
                char_count.append({'char': lchar, 'count': 1})
    return char_count

def sort_on(dict):
    return dict["count"]

def dict_sort(dict_list):
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list