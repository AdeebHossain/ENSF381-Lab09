"""
 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
 Name : lab9_exe_C . py
 Assignment : Lab 9 , Exercise C
 Author (s) : Adeeb Hossain , Ryan Razi
 Submission : Mar 20 , 2024
 Description : Fetch data by Python .
 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""

import requests
import json

def fetch_product_data(url):
    try:
        response = requests.get(url)
        # Raises an error for bad responses
        response.raise_for_status()
        # The JSON structure includes a 'products' key
        return response.json()['products']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    
def list_all_products(products):
    # iterate through all products in the product list
    for product in products:
        # print names
        print("Product Name:", product.get('title'))
        print("--------------")

def search_product(products, name):
    # linear search all products essentially
    for product in products:
        # check info associated with the product name
        if product.get('title') == name:
            print("Product found:")
            print("    Name:", product.get('title'))
            print("    ID:", product.get('id'))
            print("    Price:", product.get('price'))
            print("    Description:", product.get('description'))
            return
    print("Product not found.")

def main():
    products_url = 'https://dummyjson.com/products'
    products = fetch_product_data(products_url)

    if products:
        while True:
            choice = input("Choose an option:\n1. List all products\n2. Search for a product\n3. Exit\n> ")

            if choice == '1':
                list_all_products(products)
            elif choice == '2':
                product_name = input("Enter the product name: ")
                search_product(products, product_name)
            elif choice == '3':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Failed to fetch product data.")

if __name__ == "__main__":
    main()