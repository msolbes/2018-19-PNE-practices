import json
import termcolor

f = open("person.json", "r")

person = json.load(f)

print()

termcolor.cprint("Name: ", 'green', end='')
print(person['Firstname1'], person['Lastname1'])
termcolor.cprint("Age: ", 'yellow', end='')
print(person['age1'])

for i, num in enumerate(person["phoneNumber1"]):
    # Get the phoneNumber list
    phoneNumbers1 = person['phoneNumber1']

    # Print the number of elements int the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers1))
    termcolor.cprint(" Phone {}:".format(i), 'blue', end='')

    termcolor.cprint("  Type: ", 'red', end='')
    print(num['type'])
    termcolor.cprint("  Numer:", 'red', end='')
    print(num['number'])


termcolor.cprint("Name: ", 'green', end='')
print(person['Firstname2'], person['Lastname2'])
termcolor.cprint("Age: ", 'yellow', end='')
print(person['age2'])

for i, num in enumerate(person["phoneNumber2"]):
    # Get the phoneNumber list
    phoneNumbers2 = person['phoneNumber2']

    # Print the number of elements int the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers2))
    termcolor.cprint(" Phone {}:".format(i), 'blue', end='')

    termcolor.cprint("  Type: ", 'red', end='')
    print(num['type'])
    termcolor.cprint("  Numer:", 'red', end='')
    print(num['number'])

termcolor.cprint("Name: ", 'green', end='')
print(person['Firstname3'], person['Lastname3'])
termcolor.cprint("Age: ", 'yellow', end='')
print(person['age3'])

for i, num in enumerate(person["phoneNumber3"]):
    # Get the phoneNumber list
    phoneNumbers3 = person['phoneNumber3']

    # Print the number of elements int the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers3))
    termcolor.cprint(" Phone {}:".format(i), 'blue', end='')

    termcolor.cprint("  Type: ", 'red', end='')
    print(num['type'])
    termcolor.cprint("  Number:", 'red', end='')
    print(num['number'])
