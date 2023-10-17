import pandas as pd

# Task 1 (import excel file)
# Apply the excel document to compile a list of binary values
# In addition to the accompanying "characters."

wb = pd.read_excel("ECSProject 1.xlsx", dtype=str)

c = list(wb["Char"])
b = list(wb["Bin"])

# This line of code is used to replace the previous char \\n to \n in the char list
try:

    i = c.index("\\n")
    c[i] = "\n"
except:
    print("\\n was not found.")

# In excel file: line 69 already was input as space
# This line of code is used for reference if line 69 was input as <space>
# This line of code does not affect the char list we see in console

try:
    i = c.index(" ")
    c[i] = " "
except:
    print("<space> was not found.")


def getBin(a):
    # Characters in my lists will be from lengths one, two, or three
    # Finds the length 3 characters first, then 2 length, then 1 length

    # Find the first 3 characters in the string a and check if they're in the
    # Characters list
    if len(a) >= 3:
        a3 = a[0:2]
        for i in range(len(c)):
            if c[i] == a3:
                a = a[2:]
                binaryVal = b[i]
                return binaryVal, a
    # Find the first 2 characters and see if they are in the Characters list
    if len(a) >= 2:
        a2 = a[0:1]
        for i in range(len(c)):
            if c[i] == a2:
                a = a[1:]
                binaryVal = b[i]
                return binaryVal, a

    # Checks for one character
    if len(a) >= 1:
        for i in range(len(c)):
            if c[i] == a[0]:
                if len(a) > 1:
                    a = a[0:]
                else:
                    a = ''
                    a = a[0:]
                a = a[0:]
                binaryVal = b[i]
                return binaryVal, a

    # If no characters were found, return a string that's blank
    # And a blank binary value
    return '', ''


def getFirstBin(a):
    flag = a[0]

    # If it is a short binary value
    if flag == "0":
        # a = 5, find the first 5 values in the string
        binaryVal = a[0:5]
        a = a[5:]

    # If it is a long binary value
    else:
        # L = 7, find the first 7 values in the string
        binaryVal = a[0:7]
        a = a[7:]

    return binaryVal, a


# The function will take a binary value input and returns its
# corresponding character

def getChar(a):
    try:
        i = b.index(a)
        charVal = c[i]
    except:
        charVal = ''

    return charVal


def ttobin(file_name):
    # file variable stores the file opened through the built-in open operator in python
    file = open(file_name, "r")
    # the variable s then stores the contents of the file which in this case are the characters in the text file
    s = file.read()
    # closes the file
    file.close()
    #print(s)  # testing function
    bin_string = ""
    # This while loop is making sure that the text file being read is not an empty file
    # so that we can derive binary from it.
    while s != "":
        # print(bin_string, "\n", s)
        bin_value, s = getBin(s)
        bin_string = bin_string + bin_value

    # print(bin_string)

    # numBits is the number of bits the computer uses in to display the text file in binary
    numBits = len(bin_string)

    # bin_string takes the str value of numBits and creates a sentence using the previously obtained bin_value
    # The sentence will start with the number of bits followed by a period and end with the binary string
    bin_string = str(numBits) + "." + bin_string

    # out_file creates a new file that python will write the bin_string to, finishing the task required in task 4
    out_file = open("BinOutput.txt", "w+")
    out_file.write(bin_string)
    out_file.close()
    # print(bin_string)


def decode(file_name="BinOutput.txt"):
    # f stores the file that is opened through the python function open()
    file = open(file_name, "r")
    # s stores the data within the file, in this case it will be binary
    s = file.read()
    # this will close the aforementioned file
    file.close()

    # print(s)
    # these two variables allow us to just see the binary string.
    # it gets rid of the numBits value we found in the other function.
    i = s.index(".")
    s = s[i + 1:]
    #print(s)

    char_string = ""
    # This again checks to make sure the file isn't empty
    # it then assigns values to binVal and s using functions previously used such as getFirstbin
    # and getChar which allow us to recreate this string of characters that we can then write to
    # a new test document.
    while s != "":
        bin_value, s = getFirstBin(s)
        char_string = char_string + getChar(bin_value)
        #print(bin_value)
    # As used earlier, f stores the file opened by the open() function but this time,
    # it will write to that newly created test file "TextOutput.txt"
    nfile = open("TextOutput.txt", "w+")
    nfile.write(char_string)
    nfile.close()
    print(char_string)


def text_checker(text1, text2):
    x = open(text1, "r")  # opens first file and stores to variable
    first_file = x.read()  # reads first file and stores to varaible
    x.close()  # closes file

    y = open(text2, "r")  # opens second file and stores to variable
    second_file = y.read()  # reads second file and stores to varaible
    y.close()  # closes file

    if first_file == second_file:  # checks if files have the same contents
        return True  # if so, return True
    else:
        return False  # otherwise False.
