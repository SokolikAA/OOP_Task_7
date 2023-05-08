import view
import ask_user
import select_to_delete
import input_request
import new_contact
import change_contact
import show_contact
import menu
import phone_book


pb = phone_book.PhoneBook()


def start():
    while True:
        user_choice = menu.menu()
        match user_choice:
            case 1:
                pb.open_file()
            case 2:
                pb.save_file()
            case 3:
                book = pb.get()
                show_contact.show_contact(book)
            case 4:
                add_contact = new_contact.new_contact()
                pb.new_contact(add_contact)
            case 5:
                word = input_request.input_request('искомое слово')
                result = pb.search(word)
                show_contact.show_contact(result)
            case 6:
                new_value = change_contact.change_contact(pb.get())
                pb.change(*new_value)
            case 7:
                index = select_to_delete.select_to_delete()
                show_contact.show_contact(pb.get())
                contact = select_to_delete.select_to_delete()
                name = pb.get_name(contact)
                if ask_user.ask_user('удалить', name):
                    pb.delete(index)
            case 8:
                view.goodbye()
                break
