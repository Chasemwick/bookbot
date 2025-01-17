def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    text_num = book_word_count(book_text)
    letter_count = character_count(book_text)
    sorted_list_dict = dict_to_sorted_list(letter_count)

    print(f"--- Begin report of {path} ---")
    print(f"{text_num} words found in the document")    
    for item in sorted_list_dict:
        if item['char'].isalpha():
            print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End Report ---")
    
def get_book_text(path):  
    with open(path) as f:
        return f.read()

def book_word_count(text):
    book_words = text.split()
    count = 0 
    for word in book_words:
        count += 1
    return count

def character_count(text):
    lowered_text = text.lower()
    lower_dict = {}
    for letter in lowered_text:
        if letter in lower_dict:
            lower_dict[letter] +=1
        else:
            lower_dict[letter] = 1
    return lower_dict

def dict_sort(dict):
    return dict["count"]

def dict_to_sorted_list(dict):
    list_dict = []
    for key, value in dict.items():
        list_dict.append({"char":key, "count":value})
    list_dict.sort(reverse=True, key=dict_sort)
    return list_dict


main()           