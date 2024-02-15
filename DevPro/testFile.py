import pytest
import main as m
import test_values as testValue


# positive test for receiving all products list
def tests_1():
    assert m.get_list_and_return_list_of_products() == testValue.value_full_list


# positive test for receiving products list with defined threshold
def tests_check_boundary_value_above():
    assert m.get_list_and_return_list_of_products_with_price_higher_than(
        13.00) == testValue.value_boundary_above


def test_positive():
    assert m.get_list_and_return_list_of_products_with_price_higher_than(
        12.99) == testValue.value_positive


def tests_check_boundary_value_under():
    assert m.get_list_and_return_list_of_products_with_price_higher_than(
        12.98) == testValue.value_boundary_under
