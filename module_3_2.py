def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender or not (
            sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net") or recipient.endswith
        (".com") or recipient.endswith(".ru") or recipient.endswith(".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email("Привет!", "lion@lion.com")
send_email("Привет!", "student@student.com", "urban@student.com")
send_email("Привет!", "urban.email")
send_email("Привет!", "university.help@gmail.com", "university.help@gmail.com")
