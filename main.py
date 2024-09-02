import json

def read_file():
    try:
        print("Reading file...")
        with open('data.json', "r") as file:
            return file
    except FileNotFoundError:
        print("File not found")
        print("Creating a new file...")
        
        with open('data.json', "w") as file:
            file.write(json.dumps({}, ensure_ascii=False, indent=4))
            return read_file()
def main():
    read_file()
    print("Starting")


if __name__ == "__main__":
    main()