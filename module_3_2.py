def send_email(message, recipient, sender = "university.help@gmail.com"):
    check_com = ".com"
    check_ru = ".ru"
    check_net = ".net"
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif "@" not in recipient or "@" not in sender:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif check_com not in recipient and check_ru not in recipient and check_net not in recipient:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif check_com not in sender and check_ru not in sender and check_net not in sender:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == "university.help@gmail.com":
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
