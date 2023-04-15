def main():
    plate = input("Plate: ").lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
# проверяет начинается ли с букв (2 первые)
def start_alpha_char(plate):
    if len(plate) >= 2 and plate[:2].isalpha():
        return True
    return False

def check_if_all_alpha_chars(plate):
    if plate.isalpha():
        return True
    else:
        return(check_if_alnum(plate))

# проверяет если число символов не четное, то средний должен быть буквой
def mid_char(plate):
    if len(plate) % 2 == 1:
        mid_index = len(plate)//2
        if plate[mid_index].isalpha():
            return True
        else:
            return False
    else:
        return True

# если есть знаки пунктуации - фолз
def check_punctuation_if_exist(plate):
    for element in plate:
        if not element.isalnum():
            return False
    return True

# проверяет закачивается ли на цифры если таковые имеются
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

# проверяет длину
def correct_lenth_check(plate):
    if len(plate) >= 2 and len(plate) <= 6:
        return True
    else:
        return False



# проверяетесть ли нуль. если есть и он не в конце - фалз
def zero_in_plate(plate):
    if "0" in plate:
        if plate.endswith("0"):
            return True
        else:
            return False
    return True

# если все true то вернут true/ если хоть одно фалз - вернет фалз
def is_valid(plate):

        return all([check_if_all_alpha_chars(plate), start_alpha_char(plate), mid_char(plate), zero_in_plate(plate),
                    check_if_alnum(plate), check_punctuation_if_exist(plate), correct_lenth_check(plate)])


if __name__ == "__main__":
    main()




