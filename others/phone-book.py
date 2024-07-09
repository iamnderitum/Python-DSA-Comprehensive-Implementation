fruits = ["apple", "banana", "orange", "guava","melon"]

for idx, fruit in enumerate(fruits):
    del [idx]
    print(f"My fruits: {fruit}")

print(fruits)