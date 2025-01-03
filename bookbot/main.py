def main():
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words (text)
    num_chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_chars_dict)
    #report = get_report(chars_sorted_list)
    print("")
    print("===================")
    print("")
    print(f"CHARACTERS: {num_chars_dict}")
    print("")
    print("===================")
    print("")
    print("***** Begin report of books/frankenstein.txt *****")
    print("")
    print(f"WORDS: {num_words} words found in the document")
    print("")
    print("")
    print(chars_sorted_list)

    for each_char in chars_sorted_list:
        if not each_char["char"].isalpha():
            continue
        print(f"The '{each_char['char']}' character was found {each_char['num']} times")
    
    print("***** END REPORT *****")   
    
    
def sort_on(d):
    return d['num']    
    
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
    
def get_num_words(text):
        words = text.split()
        return len(words)

def get_chars_dict(text):
    chars = {}
    for each_char in text:
        lowered_char = each_char.lower()
        if lowered_char in chars:
            chars[lowered_char] += 1 
        else:
            chars[lowered_char] = 1
    return chars

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for each_char in num_chars_dict:
        sorted_list.append({"char": each_char, "num": num_chars_dict[each_char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



main()