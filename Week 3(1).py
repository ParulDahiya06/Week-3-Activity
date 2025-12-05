class FileReader:
    """
    A class to read a text file and return its content.
    """
    def __init__(self, filename):
        self.filename = filename
        self.content = ""

    def read_file(self):
        """Reads the file and stores content."""
        try:
            with open(self.filename, "r") as f:
                self.content = f.read()
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        return self.content

    def print_content(self):
        """Prints the content of the file."""
        if self.content:
            print("=== File Content ===")
            print(self.content)
        else:
            print("No content available. Did you read the file?")


class StarCounter(FileReader):
    """
    A subclass that extends FileReader to count '*' characters.
    """
    def count_stars(self):
        """Counts '*' characters in the file content."""
        if not self.content:
            print("Please read the file first.")
            return 0
        return self.content.count('*')


# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":
    filename = input("Enter filename: ")

    # Create object of subclass
    file_obj = StarCounter(filename)

    # Read and print file
    file_obj.read_file()
    file_obj.print_content()

    # Count '*' characters
    star_count = file_obj.count_stars()
    print(f"\nNumber of '*' characters in the file: {star_count}")
