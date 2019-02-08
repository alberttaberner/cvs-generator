import file_loader
import time
import random

def get_gender_list():
    return ["all", "male", "female"]

def valid_gender(selection):
    return (selection in get_gender_list())

def get_phone():
    value = "6"
    for i in range(9):
        value += str(int(random.random()*10))
    return value

def generate(rows, gender, file):

    start = time.time()
    def elapsed():
        return time.time() - start

    #[0] Load lists
    names_list = []
    all_gender = get_gender_list()[0]

    if(gender == all_gender or gender == get_gender_list()[1]):
        names_list.extend(file_loader.get_items('data/dist.male.first'))
    if(gender == all_gender or gender == get_gender_list()[2]):
        names_list.extend(file_loader.get_items('data/dist.female.first'))

    last_list = file_loader.get_items('data/dist.all.last')
    cities_list = file_loader.get_items('data/dist.cities.us')
    #[1] Load lists

    # Prepare counters
    # Discard last rows (POSIX 3.206 definition : A sequence of zero or more non- <newline> characters plus a terminating <newline> character.)
    name_counter = len(names_list) - 1
    last_counter = len(last_list) - 1
    cities_counter = len(cities_list) - 1

    # Attention: Overwrite existing file
    f = open(file, 'w+')

    for i in range(rows + 1):
        first_name = names_list[int(name_counter*random.random())]
        last_name = last_list[int(last_counter*random.random())]
        city_name = cities_list[int(cities_counter*random.random())]
        phone = get_phone()

        f.write("%s %s|%s|%s\n" % (first_name, last_name, city_name, phone))

    f.close()
    print("Done! It has taken %.3fs" % (elapsed()))
