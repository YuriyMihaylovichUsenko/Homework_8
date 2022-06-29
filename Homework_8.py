# Task 1

def favorite_movie(movie_name):
    print(f'My favorite movie is named {movie_name}')


# Task 2

def make_country(country_name, country_capital):
    print({country_name: country_capital})


# Task 3

def make_operation(*args):
    result = 'args[1]'
    for i in args[2:]:
        result = result + args[0] + str(i)
    print(eval(result))


make_operation('+', 7, 7, 2)
make_operation('-', 5, 5, -10, -20)
make_operation('*', 7, 6)

