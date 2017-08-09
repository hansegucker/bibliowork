log = []


def log(message, category='log'):
    category = '[' + category.upper() + ']'
    log.append([category, message])


def exit():
    import sys
    sys.exit()
