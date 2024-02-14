import pytest
import main as m


# positive test for receiving all products list
def tests_1():
    assert m.get_list_and_return_list_of_products() == "Here is a list of products: \n['Pizza', 'Sushi', 'Burger', 'Pad Thai']"


# positive test for receiving products list with defined threshold
def tests_2():
    assert m.get_list_and_return_list_of_products_with_price(
        13.00) == "Here is a list of products the price is more than 13.0: \n['Sushi', 'Pad Thai']"


def tests_3():
    assert m.get_list_and_return_list_of_products_with_price(
        1.00) == "Here is a list of products the price is more than 1.0: \n['Pizza', 'Sushi', 'Burger', 'Pad Thai']"
