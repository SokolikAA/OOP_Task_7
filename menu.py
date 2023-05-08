def menu():
    print('=====================================\n'
          '|          Телефонная книга         |\n'
          '=====================================\n'
          '|            Главное меню           |\n'
          '=====================================\n'
          '1: Открыть файл\n'
          '2: Сохранить файл\n'
          '3: Показать контакты\n'
          '4: Добавить контакт\n'
          '5: Найти контакт\n'
          '6: Изменить контакт\n'
          '7: Удалить контакт\n'
          '8: Выход\n')
    while True:
        choice = input('Введите номер меню: ')
        if choice.isdigit() and (0 < int(choice) < 9):
            return int(choice)