try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling") 
        raise IOError
    finally:
        print("Going to close the file ")
except IOError:
    print("Error: cann't find or read data")

    