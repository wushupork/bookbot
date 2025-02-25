import sys
from stats import get_num_words,get_character_count,dict_sort
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        exit(1)
    else:
        print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
        print(get_num_words(sys.argv[1])) 
        print("----------- Character Count ----------")
        for item in dict_sort(get_character_count(sys.argv[1])):
            print(f"{item['char']}: {item['count']}")
        print("=============== END ================")
    

main()