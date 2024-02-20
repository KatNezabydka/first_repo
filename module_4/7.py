'''
Everyone knows you need a pin code to access a bank's credit card. Classically, it is a combination of four digits. We need to solve the following programming task. There is a list of pin codes prepared. Write a function is_valid_pin_codes that will take as a parameter a list of these pin codes — a string of four digits and return a boolean value — whether the list is valid or not. Please make sure that there are no duplicates among these pin codes in the list, they are all stored as strings, their length is 4 characters and they contain only digits.

An example of an argument for the is_valid_pin_codes function:

['1101', '9034', '0011']
The function returns the boolean value True if the list meets all the conditions. If at least one of the conditions is violated, the value is returned — False. Provide a check for an empty list in the function argument and return the value False.
'''

def is_valid_pin_codes(pin_codes):
    if not pin_codes:
        return False

    exist_pins = set()

    for pin in pin_codes:
        if not (len(pin) == 4 and pin.isdigit()):
            return False

        if pin in exist_pins:
            return False

        exist_pins.add(pin)

    return True

pin_list = ['1101', '9034', '0011']
if is_valid_pin_codes(pin_list):
     print("The list of pin codes is valid.")
else:
    print("The list of pin codes is not valid.")