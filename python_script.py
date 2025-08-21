# Step 1: Create input.txt and write 5 lines of text
with open("input.txt", "w") as file:
    file.write("This is Line One.\n")
    file.write("This is Line Two.\n")
    file.write("This is Line Three.\n")
    file.write("This is Line Four.\n")
    file.write("This is Line Five.\n")
    file.write("This is Line Six.\n")

# Step 2: Read the contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Step 3: Count number of words
word_count = len(content.split())

# Step 4: Convert content to uppercase
upper_content = content.upper()

# Step 5: Write processed text and word count to output.txt
with open("output.txt", "w") as file:
    file.write("PROCESSED TEXT:\n")
    file.write(upper_content)
    file.write("\nWORD COUNT: {}\n".format(word_count))

# Step 6: Print success message
print("✅ output.txt has been created successfully with the processed text and word count.")