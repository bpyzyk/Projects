x = int(input ('Podaj liczbę'))
if (x%3 == 0):
  print('Podzielne przez 3')
else:
  if (x%5 == 0):
    print('Podzielne przez 5')
  else:
    print ('Niepodzielne przez 3 i 5')

y = int(input ('Podaj liczbę'))
if (y%3 == 0 or y%5 == 0):
  print ('Podzielne')
else:
  print('Niepodzielne')