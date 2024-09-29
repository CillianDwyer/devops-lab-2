numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]
average = sum(numbers) / len(numbers)
largest = max(numbers)
smallest = min(numbers)
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")