#function to count all words of an incoming string
def count_words(book_content):
       words = len(book_content.split())
       return words

#function to count all characters inside a dictionary
def count_chars(book_content):
    content_lowercase = book_content.lower()
    chars_dict = {}
    for char in set(content_lowercase):
        chars_dict[char] = content_lowercase.count(char)
    return chars_dict

def sort_key(unsorted_dictionary):
     return unsorted_dictionary["num"]


#function to define the values to sort
def sort_list(unsorted_dictionary):
    unsorted_dict_list = []
    for char, count in unsorted_dictionary.items():
        #print(char)
        if char.isalpha() is True:
           temp_dict = {"char": char, "num": count}
           unsorted_dict_list.append(temp_dict)

    unsorted_dict_list.sort(reverse=True,key=sort_key)
    return unsorted_dict_list