def main():  #we need to make sure we define main(): first, otherwise it will do nothing
    with open("books/frankenstein.txt") as f:  #opens a file using the with block, file paths are strings, use quotes
        file_contents = f.read()
    #words = file_contents.split()
    mini_text = file_contents.lower()
    #word_count = 0
    letter = {}
    #for word in words:
    #    word_count += 1
    for char in mini_text:  
        if char in letter:
            letter[char] += 1
        else:
            letter[char] = 1
    
    for key, value in letter.items():
        print(f"'{key}': {value}")
if __name__ == "__main__":
    main()