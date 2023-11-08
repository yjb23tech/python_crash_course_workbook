from name_function import get_formatted_name 

practice_function = get_formatted_name("Yinka", "Banjo")
#print(practice_function)

while True:

    first_name = input("\nWhat is your first name?\n")
    if first_name == 'q':
        break

    middle_name = input("\nWhat is your middle name?\n")
    if middle_name == 'q':
        break
    elif middle_name == ' ':
        pass

    last_name = input("\nWhat is your last name?\n")
    if last_name == 'q':
        break

    formatted_entire_name = get_formatted_name(first_name, last_name, middle_name)

    print(f"\nWelcome aboard Captain {formatted_entire_name}")

