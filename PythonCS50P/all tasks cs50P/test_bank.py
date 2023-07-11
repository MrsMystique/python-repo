from bank import value

def main():
    test_greeting_hello()
    test_with_numbers()
    test_case()
    test_h()
    test_all()

def test_greeting_hello():
    assert value("hello") == 0
    assert value("hello, newman") == 0
   

def test_with_numbers():
    assert value("123") == 100

def test_case():
    assert value("Hello") == 0

def test_h():
    assert value("h") == 20
    assert value("h, darling") == 20
    assert value("hola") == 20

def test_all():
    assert value("good day") == 100
    assert value("aloha") == 100









