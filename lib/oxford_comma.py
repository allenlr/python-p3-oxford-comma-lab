def oxford_comma(items):
    if len(items) > 2:
        first = ", ".join(items[0 : -1])
        last = ", and " + items[-1]
        return first + last
    else:
        return " and ".join(items)
