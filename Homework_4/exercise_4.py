# Необходимо удалить пустые строки из списка строк.

str_list = {1, 3, 5, 6, '', '', '', '',8, 5, 6, 9}

while '' in str_list:
    str_list.remove('')
    print(str_list)