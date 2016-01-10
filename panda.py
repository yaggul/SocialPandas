class Panda:
    def __init__(self, *args):
        self._name = args[0]
        self._email = args[1]
        self._gender = args[2]

        def is_valid_email(self):
            return "@pandamail.com" in self._email
        print(is_valid_email(self))

    def __str__(self):
        message = "{} is a {} panda with email: {}"
        return message.format(self._name, self._gender, self._email)

    def __repr__(self):
        return '{}'.format(self._name)

    def __eq__(self, other):
        return self._name == other._name and self._email == other._email and self._gender == other._gender

    def __hash__(self):
        return hash(self._name)

    def name(self):
        return self._name

    def email(self):
        return self._email

    def gender(self):
        return self._gender

    def isMale(self):
        return self.gender() == "male"

    def isFemale(self):
        return self.gender() == "female"

'''
def main():
    mitko = Panda('Mitko', 'mitko@pandamail.com', 'mail')
    alex = Panda('Alex', 'alex@pandamail.com', 'female')
    viki = Panda('Viki', 'viki@pandamail.com', 'female')
    viktor = Panda('Viktor', 'viktor@pandamail.com', 'female')
    sasho = Panda('Sasho', 'sasho@pandamail.com', 'male')
    sandy = Panda('Sandy', 'sandy@pandamail.com', 'female')



if __name__ == '__main__':
    main()
'''
