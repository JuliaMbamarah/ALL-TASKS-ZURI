# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assinment] Add your code here
    if len(str(word)) == len(str(anagram)):
        if sorted(word) == sorted(anagram):
            print("True")
        else: print("False")
    return
find_anagram("hello", "check")
find_anagram("below", "elbow")
