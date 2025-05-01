class User:

    """First name, Last name, Birthday
    Docstrings are a new concept to me"""

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday

        name_pieces = full_name.split(" ")

        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]


user = User("Dave Brown", "19042009")

print(user.first_name)
print(user.last_name)
print(user.birthday)

help(User)