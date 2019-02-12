# Example of reading a file located
# in our local filesystem

NAME = "mynotes.txt"

# Open the file
myfile = open(NAME, 'r')

print("File opened: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))

myfile.close()

f = open(NAME, 'a')
f.write("THIS IS A TEXT EXAMPLE FIR ADDUBG TO MY FILE")
f.close()
print("The end")