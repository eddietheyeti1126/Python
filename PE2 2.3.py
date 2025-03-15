def mask_creditcard(card_number):
    #Masks all but the last four digits of a credit card number.
    return '*' * (len(card_number) - 4) + card_number[-4:]


def remove_vowels(string):
    #Removes all vowels from a string.
    return ''.join(c for c in string if c.lower() not in "aeiou")


# Test cases
if __name__ == "__main__":
    print(mask_creditcard("1547615651217985"))  # '************7985'
    print(mask_creditcard("2654984951654678"))  # '************4678'
    print(mask_creditcard("7471165135377811"))  # '************7811'
    
    print(remove_vowels("Queue"))  # 'Q'
    print(remove_vowels("Education"))  # 'dctn'
    print(remove_vowels("Equation"))  # 'qtn'
