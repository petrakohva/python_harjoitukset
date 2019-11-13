todo_file = open("sales.txt", "r")
line = todo_file.readline()
while line:
    line_float = float(line)
    print (format(line_float, ".2F"))
    line = todo_file.readline()
todo_file.close()
