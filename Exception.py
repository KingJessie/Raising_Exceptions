#  Raising Exceptions

def age_validation(age):
    if age < 0:
        raise ValueError('Age needs to be more than 0')

    assert 10 < age <= 19

    return True


def name_validation(name_string):

    if ', ' not in name_string:
        raise ValueError('Incorrect, missing ","')

    name, surname = name_string.split(',')

    if not len(name) or not len(surname):
        raise ValueError('Missing name or lastname')

    return True


# Flag
isSuccessful = False
try:
    name = input('Name')
    name_validation(name)
    age = int(input('Age'))
    age_validation(age)

except ValueError as exc:
    print("Error on input: %s" % exc)
except AssertionError as exc:
    print("Error on input: %s" % exc)

else:
    print('All is good')
    isSuccessful = True
finally:
    if isSuccessful:
        print('Registered')
    else:
        print('Fail!')