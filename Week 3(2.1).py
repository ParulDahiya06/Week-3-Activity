class FileProcessor:
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, lines):
        """Write multiple lines to the file (overwrite)."""
        with open(self.filename, "w") as file:
            for line in lines:
                file.write(line + "\n")
        print("Data written successfully.")

    def append_end_message(self):
        """Append an End of File message."""
        with open(self.filename, "a") as file:
            file.write("\n--- End of File ---\n")
        print("End of File message appended.")

    def read_file(self):
        """Read and display the file content."""
        try:
            with open(self.filename, "r") as file:
                content = file.read()
                print("\nFile Content:\n")
                print(content)
        except FileNotFoundError:
            print("File not found. Please write data first.")


# ------------------------------
# Example Execution (W3-A2)
# ------------------------------

if __name__ == "__main__":
    processor = FileProcessor("output.txt")

    # Step 1: Write data
    lines_to_write = [
        "Welcome to Activity 2.",
        "We are learning file processing using OOP.",
        "This file will include an EOF message."
    ]
    processor.write_data(lines_to_write)

    # Step 2: Append End of File message
    processor.append_end_message()

    # Step 3: Display file content
    processor.read_file()
