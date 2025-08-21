# opening files
file= open("example.txt", "r") # Opens the file in read mode

# reading files
with open("example.txt", "r") as file:
    data = file.read() #.read(): Reads the entire file.
print(data)

# writes a modified version to a new file
with open("example.txt", "a") as file:
    file.write("\n""Hello, Python One!.\n")
    file.write("Hello, Python Two!.\n")
    file.write("Hello, Python Three!.\n")
    file.write("Hello, Python Four!.\n")
    file.write("Hello, Python Five!.\n")
    file.write("Hello, Python Six!.\n")