# 1. Write a function that takes the JSON data as input
# and returns a list of names of all products.
import json


def get_list_and_return_list_of_products():
    with open("fileWithText.json", "rt") as file:
        dict = json.load(file)
        list = []
        for i in dict["products"]:
            list.append(i["name"])
        file.close()
        return f"Here is a list of products: \n{list}"


get_list_and_return_list_of_products()


# 2. Write a function that takes the JSON data as
# input and a price threshold, and returns a list of
# products which price is greater than or equal to the threshold.
def get_list_and_return_list_of_products_with_price(price):
    with open("fileWithText.json", "rt") as file:
        dict = json.load(file)
        list = []
        for i in dict["products"]:
            if i["price"] > (int(price)):
                list.append(i["name"])
        file.close()
        return f"Here is a list of products the price is more than {price}: \n{list}"


get_list_and_return_list_of_products_with_price(1)
