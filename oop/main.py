from oop.classes import Car


def main():
    c1 = Car()
    c2 = Car()

    c1.model = "VFX"
    c2.model = "TFX"

    print(c1.model)
    print(c2.model)
    print(c1.__class__.company_name)
    print(c2.__class__.company_name)

    print(c1.model)
    print(c2.model)
    print(c1.__class__.company_name)
    print(c2.__class__.company_name)

    c1.company_migrations("Honda")
    print(c1.__class__.company_name)
    print(c2.__class__.company_name)

    c2.__class__.sum(10, 20)
    c1.sum(10, 20)
    c1.__class__.company_migrations("XXXX")


if __name__ == '__main__':
    main()
