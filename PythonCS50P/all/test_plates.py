from plates import is_valid


def main():
    test_start_alpha_char()
    test_correct_lenth_check()
    test_check_if_numbers_exist()
    test_check_punctuation_if_exist()
    test_alnum()
    test_all_alpha()

def test_start_alpha_char():
    assert is_valid("cdefxt")==True
    assert is_valid("AdOb")==True
    assert is_valid("YJGDCV")==True
    assert is_valid("aa")==True
    assert is_valid("50Tbdg")==False
    assert is_valid("12as")==False
    assert is_valid("64dcyo") == False
    assert is_valid("a3cdef")==False
    assert is_valid("1sdyvs")==False
    assert is_valid("1Aa") == False
    assert is_valid("-Aa") == False
    assert is_valid(" Aa") == False

def test_all_alpha():
    assert is_valid("cdefxt")==True
    assert is_valid("cdefxt")==True
    assert is_valid("aaaaaa")== True
    assert is_valid("a3cdef") == False
    assert is_valid("aa") == True
    assert is_valid("TEEKAY") == True
    assert is_valid("CS50") == True
    assert is_valid("B2MEN") == False
    assert is_valid("2GREAT") == False

def test_alnum():
    assert is_valid("aa098")== False
    assert is_valid("aa33")== True
    assert is_valid("cs50") == True
    assert is_valid("aaa23a")== False
    assert is_valid("123456") == False
    assert is_valid("1A2B3C4D") == False
    assert is_valid("123ads") == False
    assert is_valid("123ASD")== False
    assert is_valid('ABC123') == True



def test_check_if_numbers_exist():
    assert is_valid("50Tbdg") ==False
    assert is_valid("12as") == False
    assert is_valid("64dcyo") == False
    assert is_valid("a3cdef") == False
    assert is_valid("1sdyvs") == False
    assert is_valid("1a2b3c") == False
    assert is_valid("abcdef") == True
    assert is_valid("aa5aa")== False
    assert is_valid("aaaaaa")== True


def test_correct_lenth_check():
    assert is_valid("qwerty") == True
    assert is_valid("qwertyu") == False


def test_check_punctuation_if_exist():
    assert is_valid(",.;")== False
    assert is_valid("a%b")== False
    assert is_valid("a b")== False
    assert is_valid('AB.123') == False

