dictionary = {'cześć':'hello', 'mama':'mother', 'pies':'dog'}
polish_word = input('Podaj słowo po polsku\n')

if polish_word in dictionary:
  print ('Słowo po angieslku to', dictionary[polish_word])
else:
  print ('Brak w słowniku')