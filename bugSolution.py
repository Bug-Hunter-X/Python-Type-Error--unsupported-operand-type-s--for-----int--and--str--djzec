def function(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        return str(a) + str(b)

result = function(5, "hello")
print(result)  # Output: 5hello

result2 = function(5, 10) 
print(result2) #Output: 15