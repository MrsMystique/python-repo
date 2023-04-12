


def start_alpha_char(plate):
    if len(plate) >= 2 and plate[:2].isalpha():
        return True
    return False
print(f"start_alpha_char {start_alpha_char('aa')}")


def mid_char(plate):
    if len(plate) % 2 == 1:
        mid_index = len(plate)//2
        if plate[mid_index].isalpha():
            return True
        else:
            return False
    else:
        return True
print(f"mid_char {mid_char('aa')}")



def check_if_all_alpha(plate):
    if plate.isalpha():
        return True
    else:
        return check_if_alnum(plate)
print(f"check_if_alnum {check_if_all_alpha('aa')}")



def check_punctuation(plate):
    for element in plate:
        if not element.isalnum():
            return False
    return True
print(f"check_punctuation {check_punctuation('aa')}")


def check_if_alnum(plate):
    if plate.isalpha():
        return True
    half_length = len(plate) // 2
    first_half = plate[:half_length-1]
    second_half = plate[half_length:]
    if not first_half.isalpha():
        return False
    # опять засада
    elif second_half.isdigit():
        return True
    elif second_half[-1].isdigit() and second_half[-2].isdigit():
        return True
    elif second_half[-1].isdigit():
        return True
    elif second_half[-2].isdigit() and second_half[-1].isalpha():
        return False
    elif second_half[half_length-1].isdigit() and any(s.isalpha() for s in plate[half_length+1:]):
        return False


print(f"check_if_alnum {check_if_alnum('aa')}")



def check_if_all_alpha(plate):
    if plate.isalpha():
        return True
    else:
        return check_if_alnum(plate)
print(f"check_if_all_alpha {check_if_all_alpha('aa')}")



def lenth_check(plate):
    if len(plate) >= 2 and len(plate) <= 6:
        return True
    else:
        return False
print(f"lenth_check {lenth_check('aa')}")



def zero_in_plate(plate):
    if "0" in plate:
        if "0" not in plate[-1]:
            return False
        else:
            return True
    return True
print(f"zero_in_plate {zero_in_plate('aa')}")


def is_valid(plate):
        return all([check_if_all_alpha(plate), start_alpha_char(plate), mid_char(plate), zero_in_plate(plate),
                    check_if_alnum(plate), check_punctuation(plate), lenth_check(plate)])
print(f"is_valid {is_valid('aa')}")