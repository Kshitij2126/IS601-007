import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from IcecreamMachine import IceCreamMachine
# this is an example test showing how to cascade fixtures to build up state


@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm


'''
@pytest.fixture
def first_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay("$2.00", "$2.00")
    return machine


@pytest.fixture
def second_order(first_order, machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay("$2.00", "$2.00")
    return machine


def test_production_line(second_order):
    assert second_order is not None
'''


def test_one(machine):
    from IcecreamMachine import STAGE
    if machine.currently_selecting == STAGE.Container:
        assert True
    else:
        assert False


def test_two(machine):
    if machine.remaining_uses > 0:
        assert True
    elif machine.remaining_uses <= 0:
        assert False


def test_three(machine):
    if machine.remaining_toppings > 0:
        assert True
    elif machine.remaining_toppings <= 0:
        assert False


def test_four(machine):
    if machine.remaining_scoops > 0:
        assert True
    elif machine.remaining_scoops <= 0:
        assert False


def test_five(machine):
    if machine.remaining_toppings > 0:
        assert True
    elif machine.remaining_toppings <= 0:
        assert False


def test_six_one():
    icm1 = IceCreamMachine()
    icm1.handle_container("sugar cone")
    icm1.handle_flavor("vanilla")
    icm1.handle_flavor("chocolate")
    icm1.handle_flavor("next")
    icm1.handle_toppings("sprinkles")
    icm1.handle_toppings("done")
    cost1 = icm1.calculate_cost()
    assert cost1 == "$3.25"


def test_six_two():
    icm2 = IceCreamMachine()
    icm2.handle_container("waffle cone")
    icm2.handle_flavor("strawberry")
    icm2.handle_flavor("next")
    icm2.handle_toppings("sprinkles")
    icm2.handle_toppings("chocolate chips")
    icm2.handle_toppings("done")
    cost2 = icm2.calculate_cost()
    assert cost2 == "$3.00"


def test_seven():
    icm = IceCreamMachine()
    # Odering the 1st ice cream
    icm.handle_container("sugar cone")
    icm.handle_flavor("vanilla")
    icm.handle_flavor("chocolate")
    icm.handle_flavor("next")
    icm.handle_toppings("sprinkles")
    icm.handle_toppings("done")
    # Odering the 2nd ice cream
    icm.handle_container("waffle cone")
    icm.handle_flavor("strawberry")
    icm.handle_flavor("next")
    icm.handle_toppings("sprinkles")
    icm.handle_toppings("chocolate chips")
    icm.handle_toppings("done")
    # Ordering the 3rd ice cream
    icm.handle_container("cup")
    icm.handle_flavor("chocolate")
    icm.handle_flavor("vanilla")
    icm.handle_flavor("next")
    icm.handle_toppings("sprinkles")
    icm.handle_toppings("done")
    cost = icm.calculate_cost()
    icm.handle_pay(cost, "$9.50")
    assert icm.total_sales == 9.50


def test_eight():
    icm3 = IceCreamMachine()
    # Odering the 1st ice cream
    icm3.handle_container("cup")
    icm3.handle_flavor("vanilla")
    icm3.handle_flavor("next")
    icm3.handle_toppings("gummy bears")
    icm3.handle_toppings("done")
    # Odering the 2nd ice cream
    icm3.handle_container("waffle cone")
    icm3.handle_flavor("chocolate")
    icm3.handle_flavor("next")
    icm3.handle_toppings("sprinkles")
    icm3.handle_toppings("done")
    # Ordering the 3rd ice cream
    icm3.handle_container("waffle cone")
    icm3.handle_flavor("vanilla")
    icm3.handle_flavor("strawberry")
    icm3.handle_flavor("next")
    icm3.handle_toppings("sprinkles")
    icm3.handle_toppings("chocolate chips")
    icm3.handle_toppings("done")
    cost1 = icm3.calculate_cost()
    icm3.handle_pay(cost1, "$9.00")
    assert icm3.total_icecreams == 3
