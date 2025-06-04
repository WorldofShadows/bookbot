#import systems
import sys

#import from stats.py
from stats import count_words
from stats import count_chars
from stats import sort_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

#function to open the file and reading it's contents
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


#main function calling above ones and printing the word count
def main():
    #placeholder for the book variables just for my convenience. Otherwise the function calls just look like garbage
    book_file = sys.argv[1]
    book_text = get_book_text(book_file)
    book_dict = count_chars(book_text)
    book_sorted = sort_list(book_dict)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at",book_file)
    print("----------- Word Count ----------")
    print("Found",count_words(get_book_text(book_file)),"total words")
    print("--------- Character Count -------")
    for item in book_sorted:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
     
main()