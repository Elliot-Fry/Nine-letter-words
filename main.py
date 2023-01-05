
import itertools
import enchant

d= enchant.Dict("en_AU")

permutate = itertools.permutations
#first letter in given letters is the centre letter (in other words the letter which must be in each word
given_letters = ['u','t','e','n','n','o','r','c','e']


for x in given_letters: 
  y = len(given_letters) - given_letters.index(x)
  words = list((list(permutate(given_letters,y))))
  
  new_words = []
  
  for word in words:
    new_word = ""
    for letter in word:
        new_word = new_word + letter
    if new_word.count(given_letters[0]) > 0: 
      new_words.append(new_word)
    
  good_words = []
  
  for w in new_words: 
    if len(w) > 3:
      if d.check(w) == True: 
        good_words.append(w)

  
  print(good_words)
