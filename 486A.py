def calculate_f(n):
    if n % 2 != 0:
        return -n // 2
    else:
        return (n + 1) // 2
 
# Read the input value of n
n = int(input())
 
# Calculate f(n)
result = calculate_f(n)
 
# Print the result
print(result)