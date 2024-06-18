import random

number_of_friends = int(input("Enter the number of friends joining (including you):\n"))
if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {input(): 0 for _ in range(number_of_friends)}
    bill = int(input("Enter the total bill value:\n"))
    option = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if option == "Yes":
        lucky = random.choice(list(friends.keys()))
        print(f"{lucky} is the lucky one!")
        friends = {friend: round(bill / (number_of_friends - 1), 2) for friend in friends}
        friends[lucky] = 0
    else:
        print("No one is going to be lucky")
        friends = {friend: round(bill / number_of_friends, 2) for friend in friends}
    print(friends)

