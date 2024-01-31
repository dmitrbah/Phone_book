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

def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return(lines)
    except FileNotFoundError as err:
        print('Файла нет. Сначала создайте файл\n')
        return []

def show_data(data: list):
    for i in range(len(data)):
        print(f'{i+1}. {data[i]}')

def save_data(file):
    print('Введите данные контакта')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    father_name = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {father_name}, {phone_number}\n')

def search_data(contacts: list[str]):
    founded = []
    print('0 - поиск по имени')
    print('1 - поиск по фамилии')
    search_choise = input()
    if search_choise == '0':
        search_str = input('Введите имя для поиска: ')
        for contact in contacts:
            if search_str.lower() in contact.split(', ')[0].lower():
                founded.append(contact)
        return founded
    elif search_choise == '1':
        search_str = input('Введите фамилию для поиска: ')
        for contact in contacts:
            if search_str.lower() in contact.split(', ')[1].lower():
                founded.append(contact)
        return founded
    else:
        print('Некорректный ввод!')

def copy_data(data: list[str]):
    flag = True
    while flag:
        row_number = int(input(('Введите номер строки, которую надо скопировать?: ')))
        if row_number > len(data):
            print('Неверно введен номер строки!')
        else:
            print(f'Скопировать указанную строку?: {data[row_number-1]}')
            choise = input('Да/Нет? ')
            if choise.lower() == 'да':
                name = input('В какой файл скопировать данные?: ')
                with open(name+'.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{data[row_number-1]}')
                    print(f'Строка скопирована в файл {name}.txt')
                flag = False
            elif choise.lower() == 'нет':
                print('Введите номер строки заново!')
            else:
                print('Некоректный ввод выбора! Давайте заново.')

def change_data(data: str) -> str:
    name = data.split(', ')[0]
    surname = data.split(', ')[1]
    fathername = data.split(', ')[2]
    phone = data.split(', ')[3]
    print('0 - изменить имя')
    print('1 - изменить фамилию')
    print('2 - изменить отчество')
    print('3 - имзенить номер телефона')
    choise = input()
    if choise == '0':
        change_choise = input('Введите новое имя: ')
        changed = f'{change_choise}, {surname}, {fathername}, {phone}'
        return changed
    elif choise == '1':
        change_choise = input('Введите новою фамилию: ')
        changed = f'{name}, {change_choise}, {fathername}, {phone}'
        return changed
    elif choise == '2':
        change_choise = input('Введите новое отчество: ')
        changed = f'{name}, {surname}, {change_choise}, {phone}'
        return changed
    elif choise == '3':
        change_choise = input('Введите новый номер телефона: ')
        changed = f'{name}, {surname}, {fathername}, {change_choise}'
        return changed
    else:
        print('Некорректный ввод!')

def change_file(file, first_str, second_str):
    data = read_file(file)
    index = 0
    for i in range(len(data)):
        if first_str in data[i]:
            index = i
    data[index] = second_str
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(data)

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
            else:
                show_data(founded_data)
                change_file(file_name, founded_data[0], change_data(founded_data[0]))
        else:
            print('Некорректный ввод!')


if __name__ == '__main__':
    main()