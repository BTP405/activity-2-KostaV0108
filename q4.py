def statistics_decorator(func):
    def wrapper(numbers):
        count = len(numbers)
        total = sum(numbers)
        average = total / count if count > 0 else 0
        maximum = max(numbers) if numbers else None
        
        print("Numbers:", numbers)
        print("Count:", count)
        print("Average:", average)
        print("Maximum:", maximum)
    
    return wrapper

@statistics_decorator
def calculate_statistics(numbers):
    pass
def printStats(t):
    with open(t, 'r') as file:
        for line in file:
            numbers = [float(num) for num in line.strip().split()]
            calculate_statistics(numbers)
