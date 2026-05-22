import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def print_directory_tree(path, indent=""):
    for item in path.iterdir():
        if item.is_dir():
            print(indent + Fore.BLUE + "🗂 " + item.name)
            print_directory_tree(item, indent + "   ")
        else:
            print(indent + Fore.GREEN + "📁 " + item.name)

def main():
    if len(sys.argv) < 2:
        print("Error, you need to pass the path to the directory")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print("Error: there is no such path")
        return
    print(Fore.YELLOW + f"The structure of the directory: {directory_path}")
    print_directory_tree(directory_path)

if __name__ == "__main__":
    main()

