
buf = ""
def print_without_duplicates(message):
    global buf
    if buf != message:
        print(message)
    buf = ""
    buf = str(message)







