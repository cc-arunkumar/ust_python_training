even_numbers = list(map(int, input("Enter sempid: ").split(",")))
even=list(filter(lambda s :s% 2==0 , even_numbers))
print(even)