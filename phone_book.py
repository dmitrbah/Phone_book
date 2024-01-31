# Задание: Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной.

# Домашнее задание:
# Дополнить справочник возможностью копирования данных из одного файла в другой. 
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

from phone_book_operations import *

def main():
    file_name = 'phone_book.txt'
    flag = True
    while flag:
        print('0 - выход')
        print('1 - запись данных в справочник')
        print('2 - показать записи из справочника')
        print('3 - найти запись в справочнике ')
        print('4 - скопировать данные из справочника в другой файл')
        print('5 - изменить данные в справочнике')
        print('6 - удалить запись в справочнике')
        answer = input('Выберите действие: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            save_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            if founded_data == []:
                print('Ничего не найдено!')
            else:
                show_data(founded_data)
        elif answer == '4':
            data = read_file(file_name)
            copy_data(data)
        elif answer == '5':
            data = read_file(file_name)
            founded_data = search_data(data)
            if founded_data == []:
                print('Ничего не найдено!')
            elif len(founded_data) > 1:
                show_data(founded_data)
                change_index = int(input('Найдено несколько строк. Какую строку изменить?: '))
                change_file(file_name, founded_data[change_index-1], change_data(founded_data[change_index-1]))
                print('Запись изменена!')
            else:
                show_data(founded_data)
                change_file(file_name, founded_data[0], change_data(founded_data[0]))
                print('Запись изменена!')
        elif answer == '6':
            data = read_file(file_name)
            founded_data = search_data(data)
            if founded_data == []:
                print('Ничего не найдено!')
            elif len(founded_data) > 1:
                show_data(founded_data)
                change_index = int(input('Найдено несколько строк. Какую строку удалить?: '))
                change_file(file_name, founded_data[change_index-1], [])
                print('Запись удалена!')
            else:
                show_data(founded_data)
                change_file(file_name, founded_data[0], [])
                print('Запись удалена!')
        else:
            print('Некорректный ввод!')

if __name__ == '__main__':
    main()