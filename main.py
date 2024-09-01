import wikipedia


while True:
  user_input = input('Enter a term: ')
  response = wikipedia.summary(user_input)
  if user_input in response:
    print("Bot: ", response)
    print('\n')
  else:
    print("Not found!!")
