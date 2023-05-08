def new_contact():
    print()
    phone = correct_phone()
    name = input('Введите имя и фамилию контакта: ')
    comment = input('Введите коментарий: ')
    print()
    return {'phone': phone, 'name': name, 'comment': comment}