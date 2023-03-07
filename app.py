import file_handler

import math
import sys

def main():
    data = file_handler.load_excel_data(r'in/Kategorien.xlsx')

    sleep_timer = 10
    ok_streak = 0

    total = sum(1 for item in data.iterrows())
    current = 1
    int_length = int(math.log(total, 10)) + 1
    
    for item in data.iterrows():
        filename = "{}___{}___{}".format(item[1][4][-3:], item[1][1], item[1][2]).replace(' ', '_').replace('/', '_')
        category_link = "https://www.vhs-karlsruhe.de/qr-kategorie/KAT{}".format(item[1][4][-3:])

        print("[{current:0>{length}}/{total}] {sleep}s".format(current=current, length=int_length, total=total, sleep=sleep_timer))
        current = current + 1

        res = file_handler.save_to_out(category_link, filename, sleep_timer)
        print()

        if res > 0:
            sleep_timer = sleep_timer + 1
            ok_streak = 0
        elif res == 0:
            ok_streak = ok_streak + 1

        if ok_streak * sleep_timer >= 100:
            sleep_timer = max(0, sleep_timer - 1)
            ok_streak = 0


def test():
    data = file_handler.load_excel_data(r'in/Kategorien.xlsx')
    
    for item in data.iterrows():
        print('-----')
        print("https://www.vhs-karlsruhe.de/qr-kategorie/KAT{}".format(item[1][4][-3:]))

if __name__ == "__main__":
    main()