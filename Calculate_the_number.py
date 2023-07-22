def up_low(s):
    
    upper = []
    lower = []

    for letter in s:
      if letter.isupper():
        upper.append(letter)
      elif letter.islower():
        lower.append(letter)

    print(f"Number of upper case characters: {len(upper)}")
    print(f"Number of lower case characters: {len(lower)}")


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)