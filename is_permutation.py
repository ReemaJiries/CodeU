def is_permutation(str1 = "", str2 = ""):
    if str1 is None and str2 is None:
        return True
    if str1 is None or str2 is None:
        print("Invalid Input: one of the strings is None")
        return
    if str1 is "" or str2 is "":
        print("Missing Input: missing one or more of the 2 required positional arguments")
        return
    if type(str1) != str or type(str2) != str:
        print("Invalid Input: String1 or Stirng2 is not string type")
        return
    if not(str1.isalpha()) or not(str2.isalpha()):
        print("Invalid Input: Strings should contain just alphabet letter")
        return
    dict = {}
    str1 = str1.lower()
    str2 = str2.lower()
    for letter in str1:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    for letter in str2:
        if letter in dict:
            dict[letter] -= 1
        else:
            return False
    for value in dict.values():
        if value != 0:
            return False
    return True
