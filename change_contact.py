import show_contact


def change_contact(book: list):
    show_contact.show_contact(book)
    choice = int(input('Выберите контакт, который хотите изменить: '))
    phone = input('Введите новый номер вида: +7 код номер без пробелов или Enter если оставить без изменений: ')
    name = input('Введите новое имя или Enter если оставить без изменений: ')
    comment = input('Введите новый коментарий или Enter если оставить без изменений: ')
    return choice - 1, {'phone': phone if phone else book[choice - 1].get('phone'),
                        'name': name if name else book[choice - 1].get('name'),
                        'comment': comment if comment else book[choice - 1].get('comment')}
