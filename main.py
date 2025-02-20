def sort_on(dict):
        return dict["count"]

def main():  #we need to make sure we define main(): first, otherwise it will do nothing
    with open("books/frankenstein.txt") as f:  #opens a file using the with block, file paths are strings, use quotes
        file_contents = f.read()
    words = file_contents.split()
    mini_text = file_contents.lower()
    word_count = 0
    letter = {}
    #alphabet = letter.isalpha()
    for word in words:
        word_count += 1
    for char in mini_text:  
        if char.isalpha():  #checks if the char is an alphabet and not numerical
            if char not in letter:
                letter[char] = 0    #this starts the counter for letters now and icrements it below       
            letter[char] += 1
    
    char_list = []
    for char, count in letter.items():
        char_list.append({"char": char, "count": count})
    
    
    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} total words found in the document")
    print(" ")

    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")

    print("--- End report---")
if __name__ == "__main__":
    main()