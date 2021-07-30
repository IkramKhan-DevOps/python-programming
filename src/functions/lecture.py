
def func_positional_args(n1, n2, n3):
    print("func_positional_args")


def func_keyword_args(a1, a2, a3):
    print("func_keyword_args")


def func_arb_args(*args):
    print("func_arb_args: ", args)


def func_key_arb_args(**kwargs):
    print("func_key_arb_args: ", kwargs)


def func_def_args(n1=10, n2=30, n4=50):
    print("func_def_args")


def hard_task(name, *subjects, creadit_hour=3, **marks):
    """
    :param name              1st positional
    :param subjects:         2nd arbitrary
    :param creadit_hour:     3rd default args
    :param marks:            4th keyword args
    :return:
    """
    print(name, subjects, creadit_hour, marks)


def hard_task2(*subjects, **marks):
    """
    :param name              1st positional
    :param subjects:         2nd arbitrary
    :param creadit_hour:     3rd default args
    :param marks:            4th keyword args
    :return:
    """
    print(subjects, marks)


if __name__ == '__main__':
    # func_positional_args(10, 20, 30)
    # func_positional_args(n3=30, n2=20, n1=10)
    # func_positional_args(10, n3=30, n2=20)

    # func_arb_args(args=(1, 2, 3, 4))
    func_key_arb_args(kwargs={'1': 1})
    hard_task("MARK", 1, 2, 3, 4, marks={"1":1, "2": 2})
    hard_task2(subjects=(1, 2, 3), marks={"1":1, "2": 2,})




