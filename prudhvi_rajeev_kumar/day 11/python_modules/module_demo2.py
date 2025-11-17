import random

# def generate_order_id():
#     return f"{random.randint(100000, 999999)}"

# if __name__ == "__main__":
#     for _ in range(1):
#         print(generate_order_id())

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]
original_fruit_list = fruits.copy()
random.shuffle(fruits)
print(f"Original fruit list: {original_fruit_list}")
print(f"Shuffled fruit list: {fruits}")
selected_fruit = random.choice(fruits)
print(f"Randomly selected fruit: {selected_fruit}")    
