logged = []


def log(message, category='log'):
    category = '[' + category.upper() + ']'
    logged.append([category, message])


def exit():
    import sys
    sys.exit()
