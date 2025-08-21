try:
    filename=input("Please Insert a filename: ")

    with open(f"{filename}", "r") as file:
        content = file.read()
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Create a new output file name
        output_file = "modified_" + filename

        # Write the modified content to the new file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Modified content written to '{output_file}' successfully.")
except FileNotFoundError:
    print("File not found. Please check the filename.")