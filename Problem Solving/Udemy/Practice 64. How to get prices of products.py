products = {
    "Grape": 5.9,
    "Guava": 4.5,
    "Mango": 4.8,
    "Cashew": 8,
    "Banana": 3.0,
    "Pear": 5.8,
}


for pro, price in products.items():
    print(pro, "= ", price)

cost = 0.0
while True:
    pro = input("Select products (n = nothing): ")
    if pro == "n":
        break
    qty = int(input("Number of products? "))
    cost = cost + (products[pro] * qty)

print("Price of products:", cost)

