class Borsch:  # креслення, рецепт, інструкція

    value = 2  # атрибут класу, аргумент класу, параметр класу, поля класу(змінна класу)

    beet = True  # можуть юути будь-якого типу

    meat = 'pork'

    def boiled(self, temperature):  # метод обʼекту класа (функція обʼекту класу)

        if temperature > 100:

            return 'You boiled borsch'

        else:

            return 'You need more'


odesa_borsch = Borsch()


class Human:
    name=""
    age=20
    profession="builder"
    def eat(self):
        return "you eat "

class Pilot(Human):
    pilot=Human()

    name = Human.name

