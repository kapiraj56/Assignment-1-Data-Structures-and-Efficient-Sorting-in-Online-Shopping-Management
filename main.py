import time
class Product:
    def __init__(self, ID, Name, Price, Category):
        self.ID = ID
        self.Name = Name
        self.Price = Price
        self.Category = Category

    @staticmethod
    def load_data_product(file_name):
        print("Loading product data from list...")
        products = []
        with open(file_name, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                product = Product(data[0], data[1], float(data[2]), data[3])
                products.append(product)

        print("Size of data:", len(products))
        return products

    @staticmethod
    def insert_product(products, new_inventory_product):

        products.append(new_inventory_product)

        print("Size of data:", len(products))

    @staticmethod
    def update_product(products, product_id, new_product_detail):

        for product in products:
            if product_id == product.ID:
                product.Name = new_product_detail['name']
                product.Price = new_product_detail['price']
                product.Category = new_product_detail['category']


    @staticmethod
    def delete_product(products, product_id):

        products[:] = [product for product in products if product.ID != product_id]

        print("Size of data:", len(products))

    @staticmethod
    def search_for_product(products, key):

        found_products = []
        for product in products:
            if key in (product.Name, product.ID):
                found_products.append(product)

        return found_products

    @staticmethod
    def bubble_sort(products):

        n = len(products)
        for i in range(n):
            for j in range(0, n-i-1):
                if products[j].Price > products[j+1].Price:
                    products[j], products[j+1] = products[j+1], products[j]


    @staticmethod
    def measuring_sorting_time(products, sorting_function):
        start_time = time.time()
        sorting_function(products)
        end_time = time.time()
        return end_time-start_time

    @staticmethod
    def generate_sorted_data(size):
        products = [Product(str(i), f"Product{i}", i, "Category") for i in range(1, size+1)]
        return products

    @staticmethod
    def generate_sorted_reverse_data(size):
        products = [Product(str(i), f"Product{i}", size - i, "Category") for i in range(size, 0, -1)]
        return products


product_data = Product.load_data_product("product_data.txt")


time_sorted = Product.measuring_sorting_time(product_data, Product.bubble_sort)
print("The time taken to sort already sorted data:", time_sorted)

time_reverse_sorted = Product.measuring_sorting_time(product_data[::-3], Product.bubble_sort)
print("The time taken to sort reverse sorted data:", time_reverse_sorted)

new_product = Product('99999', 'New Product', 99.99, 'Misc')
Product.insert_product(product_data, new_product)

update_details = {'name': 'Updated Name', 'price': 199.99, 'category': 'Updated Category'}
Product.update_product(product_data, '41355', update_details)

Product.delete_product(product_data, '66237')

search_results = Product.search_for_product(product_data, 'Knife Set ASRHX')

Product.bubble_sort(product_data)

print("\nFinal sorted product data:")
for product in product_data:
    print(f"ID: {product.ID}, Name: {product.Name}, Price: {product.Price}, Category: {product.Category}")


