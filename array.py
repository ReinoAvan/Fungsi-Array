from tabulate import tabulate

items = [
    {"name": "Indomie", "price": 3000, "rating": 5, "likes": 150},
    {"name": "Laptop", "price": 4000000, "rating": 4.5, "likes": 123},
    {"name": "Aqua", "price": 3000, "rating": 4, "likes": 250},
    {"name": "Smart Tv", "price": 4000000, "rating": 4.5, "likes": 42},
    {"name": "Headphone", "price": 4000000, "rating":3.5, "likes":90},
    {"name": "Very Smart TV", "price": 4000000, "rating":3.5, "likes":87},
]

def sort_items(items):
    return sorted(items, key=lambda x: (x["price"], x["rating"], x["likes"]))

def add_item(items, name, price, rating, likes):
    items.append({"name": name, "price": price, "rating": rating, "likes": likes})
    return items

print(tabulate(sort_items(items), headers="keys", tablefmt="pretty"))

items = add_item(items, "Mainan", 50000, 4, 70)
items = add_item(items, "Buku", 10000, 4, 60)
items = add_item(items, "Helikopter", 10000000, 5, 298)
print(tabulate(sort_items(items), headers="keys", tablefmt="pretty"))
