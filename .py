import random

options = ('Piedra', 'Papel', 'Tijera')
computer_wins = 0
user_wins = 0
Rounds = 1

while True: 
  
  print('*' * 10)
  print('Round', Rounds)
  print('*' * 10)
  print('computer_wins', computer_wins)
  print('user_wins', user_wins)
  
  user_option = input('Piedra, Papel o Tijera => ')
  user_option = user_option.capitalize()
  Rounds += 1
  if not user_option in options:
    print('esa opcion no es valida')
    continue 
  computer_option = random.choice(options)
  
  print('User option =>', user_option)
  print('computer_option =>', computer_option)
  
  if user_option == computer_option: 
    print('Empate')
  elif user_option == 'Piedra':
    if computer_option == 'Tijera':
      print('Piedra gana a Tijera')
      print('user gano')
      user_wins +=1
    else:
      print('Papel gana a Piedra')
      print('computer gano')
      computer_wins +=1
  elif user_option == 'Papel':
    if computer_option == 'Piedra':
      print('Papel gana a Piedra')
      print('user gano')
      user_wins +=1
    else:
      print('Tijera gana a Papel')
      print('computer gano')
      computer_wins +=1
  elif user_option == 'Tijera':
    if computer_option == 'Papel':
      print('Tijera gana a Papel')
      print('user gano')
      user_wins +=1
    else:
      print('Piedra gana a Tijera')
      print('computer gano')
      computer_wins +=1

  if computer_wins == 2:
    print('El ganador es la computadora')
    break
  if user_wins == 2:
    print('El ganador es el usuario')
    break

  


  
