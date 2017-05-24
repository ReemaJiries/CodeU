from is_permutation import is_permutation

if __name__ == '__main__':
    assert is_permutation('asks', 'skas')
    assert not is_permutation('abcd', 'efgh')
    assert not is_permutation('', 'a')
    assert not is_permutation('a', '')
    assert is_permutation('s', 's')
    assert not is_permutation('', '')
    assert not is_permutation(None, '')
    assert is_permutation(None, None)
    assert not is_permutation("", None)
    assert is_permutation("Listen", "Silent")
    assert is_permutation("Triangle", "Integral")
    assert not is_permutation("Apple", "Pabble")
    assert not is_permutation(5, "Pabble")
    assert not is_permutation("Pabble", 5)
    assert not is_permutation(6, 5)
    assert not is_permutation("Tria_ngle", "_Integral")
    assert not is_permutation("Tria ngle", " Integral")

    print("Testing very long inputs")
    str1 = "avDef"
    str2 = ""
    for i in range(1000):
      str1 += "a"
      str2 += "a"
    str2+= "avDef"
    str3 = "vvvv"
    assert is_permutation(str1, str2)
    assert not is_permutation(str1, str3)
    assert not is_permutation(str3, str2)

