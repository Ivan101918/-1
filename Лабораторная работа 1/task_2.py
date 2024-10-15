disketa_volume = 1.44 * 1024 * 1024 # объём дискеты в байтах
pages = 100
strings_in_page = 50
chars_in_string = 25
char_vol = 4

book = pages * strings_in_page * chars_in_string * char_vol

fit_books = int(disketa_volume // book)






print("Количество книг, помещающихся на дискету:", fit_books)
