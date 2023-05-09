# 3.4. На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.

# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.

# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

# Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.

# Sample Input:
# a3b4c2e10b1 Sample Output:
# aaabbbbcceeeeeeeeeeb


def to_full(hash_str):
    full_str = ''
    i = 1 #start from 2dn symb
    num = 0 #q-ty of symbols
    num_rec = False # is number of syblos is recording
    symb = hash_str[0]
    while i < len(hash_str):
        if hash_str[i].isdigit() and num_rec == False: #проверяем число ли это?
            num = int(hash_str[i])
            num_rec = True
        elif hash_str[i].isdigit() and num_rec == True: #проверяем число ли это и было ли число до этого
            num = num * 10 + int(hash_str[i])    
        else:
            full_str += symb * num
            symb = hash_str[i]
            num_rec = False
            num = 0
        i += 1
    full_str += symb * num
    return full_str

# hash = 'a3b4c2e10b1'
# print(to_full(hash))

with open ('dataset_3363_2.txt') as inf:
    s1 = inf.readline()
with open('dataset To full.txt', 'w') as my_file:
    my_file.write(to_full(s1))