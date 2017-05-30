from is_permutation import is_permutation

if __name__ == '__main__':
    print("Testing valid sample inputs:")
    assert is_permutation('asks', 'skas')
    assert not is_permutation('abcd', 'efgh')
    assert is_permutation(None, None)
    assert is_permutation("Listen", "Silent")
    assert is_permutation("Triangle", "Integral")
    assert not is_permutation("Apple", "Pabble")
    assert is_permutation('s', 's')
    print("Done")
          
    print("Testing Invalid inputs:")
    #Missing Input: missing one or more of the 2 required positional arguments
    assert not is_permutation('', 'a')
    assert not is_permutation('a', '')
    assert not is_permutation('', '')
    
    #Invalid Input: one of the strings is None
    assert not is_permutation(None, '')
    assert not is_permutation("", None)
    
    #Invalid Input: String1 or Stirng2 is not string type
    assert not is_permutation(5, "Pabble")
    assert not is_permutation("Pabble", 5)
    assert not is_permutation(6, 5)
    
    #Invalid Input: Strings should contain just alphabet letter
    assert not is_permutation("Tria_ngle", "_Integral")
    assert not is_permutation("Tria ngle", " Integral")
    print("Done")

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
    print("Done")
    
    print("All tests have been passed")
