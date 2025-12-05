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
        """Prints the content of the file and an EOF message."""
        if self.content:
            print("\n--- File Content Start ---\n")
            print(self.content)
            print("\n--- End of File ---")   # <<< Added EOF Message
        else:
            print("No content to display.")


class StarCounter(FileReader):
    """
    A subclass of FileReader that counts '*' characters.
    """
    def count_stars(self):
        """Counts number of '*' in the file content."""
        return self.content.count('*')


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
