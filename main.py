import file_creator as creator
import sys
import os.path

# Wait for manual number of rows insertion
def ui_get_row(prompt):
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

# Wait for gender selection
def ui_get_gender(prompt):
    while True:
        try:
            value = str(input(prompt))
        except ValueError:
            print('\nSorry, I didn\'t understand that.')
            continue

        try:
            idx = creator.get_gender_list().index(value)
            break
        except ValueError:
            print('\nSelect a valid option: ' + ','.join(creator.get_gender_list()))
            continue
    return value

# Wait for filename insertion
def ui_get_file_name(prompt):
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
    args = len(sys.argv)
    if args == 1:
        required_rows = ui_get_row('\nHow many rows do you wish to generate?\n')
        gender_type = ui_get_gender('\nWhich gender do you need for the name fields?\nOptions are: ' + ', '.join(creator.get_gender_list()) + "\n")
        filename = ui_get_file_name('\nWhere do you want the data to be saved?\n')

        creator.generate(required_rows, gender_type, filename)

    elif args == 4:
        filename = sys.argv[1]
        rows = sys.argv[2]
        gender = sys.argv[3]

        # Check if rows are a valid integer
        try:
            rows_int = int(rows)
        except ValueError:
            print("Invalid number of rows type.")
            sys.exit(1)

        if(len(filename) == 0):
            print("Invalid filename.")
        elif(rows_int == 0):
            print("Invalid number of rows.")
        elif not(creator.valid_gender(gender)):
            print(
            "Invalid gender.\n"
            'Available genders are: ' + ', '.join(creator.get_gender_list())
            )
        else:
            creator.generate(rows_int, gender, filename)

    else:
        print (
        'Invalid arguments. Try one of the following commands:\n'
        '   \'python '+__file__+'\n'
        '   \'python '+__file__+' filename rows_to_generate gender_type\'.\n'
        'Available genders are: ' + ', '.join(creator.get_gender_list())
        )

if __name__ == "__main__":
    main()
