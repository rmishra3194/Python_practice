fruit = 'banana'
#index = 0
'''while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1'''

    
'''prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    print(letter + suffix)'''

#print(fruit[1:1])

#print(fruit[1:]) 

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

#print(find('banana', 'a'))

#print(find('banana', 'c'))

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

#print(find('banana', 'a', 2))

def count(word, letter):
    count = 0
    for i in word:
        if i == letter:
            count = count + 1
    return count

#print(count('banana', 'b'))

def in_both(word1 , word2):
    for letter in word1:
        if letter in word2:
            print(letter)

#in_both('apple', 'orange')

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2)-1

    while j >= 0:
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1

    return True

#print(is_reverse('apple' , 'mango'))

#print(fruit.count('a'))

#print(fruit[0:5:2])

#print(fruit[::-1])

def is_palindrome(text):
    if text == text[::-1]:
        return True
    return False

#print(is_palindrome('taM'))

def any_lowercase(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        
    return True

print(any_lowercase5('MAMA'))


def rotate_word(word: str, shift: int) -> str:
  result = []

  for char in word:
    if "a" <= char <= "z":
      # Shift within lowercase 'a'-'z' (0..25) and wrap with modulo 26
      new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
      result.append(new_char)
    elif "A" <= char <= "Z":
      # Shift within uppercase 'A'-'Z' (0..25) and wrap with modulo 26
      new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
      result.append(new_char)
    else:
      # Leave spaces, punctuation, and numbers unchanged
      result.append(char)

  return "".join(result)
