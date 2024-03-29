# Функции для работы со телефонным справочником

def read_file(file) -> list:
    '''
    Функция считывает строки с файла и передает их в выводимый список
    '''
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return(lines)
    except FileNotFoundError as err:
        print('Файла нет. Сначала создайте файл\n')
        return []

def show_data(data: list):
    '''
    Функция выводит строки списка
    '''
    for i in range(len(data)):
        print(f'{i+1}. {data[i]}')

def save_data(file):
    '''
    Функция записывает имя, фамилию, отчество и номер телефона в файл справочника.
    В случае если файла с указанным именем не существует - соответствующий файл будет создан.
    '''
    print('Введите данные контакта')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    father_name = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {father_name}, {phone_number}\n')

def search_data(contacts: list[str]):
    '''
    Функция находит по имени или фамилии строку с данными из поступаемого списка контактов
    '''
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
    '''
    Функция копирует выбранные строки в новый файл
    '''
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
    '''
    На вход функции поступает строка, которую требуется изменить. Функция возвращает новую строку
    с измененным именем, фамилией, отчеством и номером телефона
    '''
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
    '''
    Функция меняет строки в файле. Если строка на которую надо изменить = [], то указанная строка
    будет удалена
    '''
    data = read_file(file)
    index = 0
    for i in range(len(data)):
        if first_str in data[i]:
            index = i
    if second_str == []:
        data.pop(index)
    else:
        data[index] = second_str
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(data)
