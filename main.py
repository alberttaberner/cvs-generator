import file_creator

def get_row(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0 or value > 200000:
            print("Please select a valid [0-200k].")
            continue
        else:
            break
    return value

def get_gender(prompt):
    while True:
        try:
            value = str(input(prompt))
        except ValueError:
            print('\nSorry, I didn\'t understand that.')
            continue

        try:
            idx = file_creator.get_gender_list().index(value)
            break
        except ValueError:
            print('\nSelect a valid option: ' + ','.join(file_creator.get_gender_list()))
            continue
    return value

def get_file_name(prompt):
    while True:
        try:
            value = str(input(prompt))
        except ValueError:
            print('\nSorry, I didn\'t understand that.')
            continue

        if(len(value) > 0):
            break
        else:
            print("\nPlease insert a valid name.")
            continue
    return value

def main():

    required_rows = get_row('\nHow many rows do you wish to generate?\n')
    gender_type = get_gender('\nWhich gender do you need for the name fields?\nOptions are: ' + ', '.join(file_creator.get_gender_list()) + "\n")
    file_name = get_file_name('\nWhere do you want the data to be saved?\n')

    file_creator.generate(required_rows, gender_type, file_name)

if __name__ == "__main__":
    main()
