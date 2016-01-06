class Panda:
    def __init__(self, name, email, gender):
        self._name = name
        self._email = email
        self._gender = gender

    def __str__(self):
        message = "{} is a {} panda with email: {}"
        return message.format(self._name, self._gender, self._email)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._name == other._name & self._email == other._email & self._gender == other._gender

    def __hash__(self):
        return str(self._amount)

    def is_valid_email(self):
        return "@pandamail.com" in self._email

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


ivo = Panda("Ivo", "ivo@pandamail.com", "male")

print(ivo.name())
print(ivo.email())
print(ivo.gender())
print(ivo.isMale())
print(ivo.isFemale())
print(ivo)
