# 1. Write a function that takes the JSON data as input
# and returns a list of names of all products.
import json


def get_list_and_return_list_of_products():
    with open("fileWithText.json", "rt") as file_1:
        dict_products = json.load(file_1)
        list_products = []
        for i in dict_products["products"]:
            list_products.append(i["name"])
        file_1.close()
        return f"Here is a list of products: \n{list_products}"


get_list_and_return_list_of_products()


# 2. Write a function that takes the JSON data as
# input and a price threshold, and returns a list of
# products which price is greater than or equal to the threshold.
def get_list_and_return_list_of_products_with_price(price):
    with open("fileWithText.json", "rt") as file:
        dict_products = json.load(file)
        list_products = []
        for i in dict_products["products"]:
            if i["price"] > (int(price)):
                list_products.append(i["name"])
        file.close()
        return f"Here is a list of products the price is more than {price}: \n{list_products}"


get_list_and_return_list_of_products_with_price(1)
