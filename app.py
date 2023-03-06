import file_handler

import sys

def main():
    file_handler.save_to_out(sys.argv[1], sys.argv[2])

def test():
    pass
    #file_handler.save_to_out(['a', 'hannes', 'dada', 'dadada', 'ar389u[3f9jafofj]', 'schnelligkeit', 'äääää', 'Gammelfl31sch', '1111111111111111111111111111111111111111111', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])

if __name__ == "__main__":
    main()