try:
    fh = open("testfile", "w")   
    fh.write("This is my test file for exception handling") 
except IOError:
    print("Error: cann't find or read data")
else:
    print("Written content in the file successfully")
    fh.close()