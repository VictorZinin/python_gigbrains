menu = ['Главное меню',
        'Открыть файл',
        'Сохранить файл',
        'Показать контакты',
        'Создать контакт',
        'Найти контакт',
        'Изменить контакт',
        'Удалить контакт',
        'Выход']
input_menu = 'Выберите пункт меню: '
input_menu_error = f'Ввести нужно ЧИСЛО (от 0 до {len(menu)-1})'

load_successfull = 'Телефонная книга загружена успешно!'
save_successfull = 'Телефонная книга сохранена успешно!'

empty_book_error = 'Телефонная книга пуста или не открыта'

input_contact = ['Введите имя нового контакта: ',
                 'Введите номер телефона: ',
                 'Введите коментарий: ']

input_edit_contact = ['Введите имя нового контакта или нажмите ENTER чтобы оставить без изменеий: ',
                      'Введите номер телефона или нажмите ENTER чтобы оставить без изменеий: ',
                      'Введите коментарий или нажмите ENTER чтобы оставить без изменеий: ']

input_edit_contact_id = 'Введите ID контакта, который хотите изменить: '
input_del_contact_id = 'Введите ID контакта, который хотите удалить: '

input_search_word = 'Введите ключевое слово для поиска: '

operation = ['создан', 'изменен', 'удален']

def contact_action(name: str, action: str) -> str:
    return f'Контакт {name} успешно {action}!'

def not_find(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдены!'

confirm_changes = 'У вас есть несохранённые изменения! Сохранить? yes/no'
exit_program = 'До свидания, до новых встречь!'
