logged = []


def log(message, category='log'):
    category = '[' + category.upper() + ']'
    logged.append([category, message])


def exit():
    import sys
    sys.exit()


def gen_barcode(book_id):
    id_str = str(book_id)
    id_len = len(id_str)
    while (id_len < 13):
        id_str = id_str + '0'
        id_len = len(id_str)
    return int(id_str)
