# opening files
file= open("example.txt", "r") # Opens the file in read mode
print(file)
# reading files
with open("example.txt", "r") as file:
    data = file.read() #.read(): Reads the entire file.
                        #.readline(): Reads a single line at a time.
                        #.readlines(): Reads all lines and returns a list.
print(data)

# writing and appending to the file
with open("example.txt", "a") as file:
    file.write("Hello, Python!") #write(): Overwrites content, while append() allowing adding without deleting.