import sys
from pathlib import Path
from colorama import Fore, Style, init

# Initialize Colorama to make it work on Windows as well
init()

def list_directory_contents(path, level=0):
    """ Recursively list the contents of a directory showing directories and files in different colors. """
    # Make sure the path is a directory
    if not path.is_dir():
        raise ValueError("Provided path is not a directory")
    
    # Iterate over the items in the directory
    for item in path.iterdir():
        # Create an indent for sub-items
        indent = '    ' * level
        if item.is_dir():
            print(Fore.BLUE + f"{indent}{item.name}/")
            # Recurse into the subdirectory
            list_directory_contents(item, level + 1)
        else:
            print(Fore.GREEN + f"{indent}{item.name}")
    print(Style.RESET_ALL)

def main():
    # Check if the path is provided
    if len(sys.argv) != 2:
        print("Usage: python <script> <path_to_directory>")
        sys.exit(1)
    
    directory_path = Path(sys.argv[1])
    
    # Handle exceptions if the path is invalid
    try:
        list_directory_contents(directory_path)
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        print(Style.RESET_ALL)
        sys.exit(1)

if __name__ == "__main__":
    main()
