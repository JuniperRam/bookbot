def main():  #we need to make sure we define main(): first, otherwise it will do nothing
    with open("books/frankenstein.txt") as f:  #opens a file using the with block, file paths are strings, use quotes
        file_contents = f.read()
    words = file_contents.split()
    word_count = 0
    for word in words:
        word_count += 1
    print (word_count)
if __name__ == "__main__":
    main()

