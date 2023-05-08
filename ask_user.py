def ask_user(action: str, name: str):
    answer = input(f'Уверены что хотите {action} контакт {name}? Если да то нажмите "y"!')
    if answer == 'y':
        return True
    else:
        return False