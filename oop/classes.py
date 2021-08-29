
class Car:
    company_name = "Corolla"

    def __init__(self):
        self.model = None
        self.__private = None

    @classmethod
    def company_migrations(cls, company_name):
        cls.company_name = company_name

    @staticmethod
    def sum(n1, n2):
        print()


class Animal:

    def __init__(self, category, name, description):
        self.category = category
        self.name = name
        self.description = description
        self.__parent_private = 'PP1'


class Sky(Animal):

    def __init__(self, category, name, description, wings_size, beak_color):
        super().__init__(category, name, description)
        self.wings_size = wings_size
        self.beak_color = beak_color
        self.__parent_private = 'CPS1'


class Land(Animal):

    def __init__(self, category, name, description, legs):
        super().__init__(category, name, description)
        self.legs = legs
        self.__parent_private = 'CPL1'
