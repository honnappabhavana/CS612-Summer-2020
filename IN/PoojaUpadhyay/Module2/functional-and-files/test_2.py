try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling")
except IOError:
    print("Error: cann't find file or read data")
else:
    print("Written content in the file successfully")