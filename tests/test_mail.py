def test_mail_sender(mail):
    assert mail.sender == 'holmes@yandex.ru'


def test_mail_receiver(mail):
    assert mail.receiver == 'watson@yandex.ru'
