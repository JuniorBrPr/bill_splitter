number_of_friends = int(input("Enter the number of friends joining (including you):\n"))
if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {input(): 0 for _ in range(number_of_friends)}
    bill = int(input("Enter the total bill value:\n"))
    for friend in friends:
        friends[friend] = round(bill / number_of_friends, 2)
    print(friends)
