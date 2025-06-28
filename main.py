from time import time

def delete_punctuation(text: str) -> str:
    clear_text = ""
    for sym in text:
        if sym=='\n':
            clear_text+=' '
        
        if sym.isalpha() or sym==' ':
            clear_text+=sym
    
    clear_text = clear_text.lower()

    return clear_text

def count_letters(text: str) -> dict[str, int]:
    letter_count = {}
    for let in text:
        if not let in letter_count:
            letter_count[let] = 1
            continue
        letter_count[let] += 1
    
    del letter_count[' ']

    return letter_count


def main():
    path = "text.txt"
    with open(path, 'r') as file:
        full_text = file.read()
    
    text = delete_punctuation(full_text)
    words = text.split()
    letter_count = count_letters(text)
    print(letter_count)

if (__name__ == "__main__"):
    main()