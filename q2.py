import matplotlib.pyplot as plt

def graphSnowfall(t):
    # Read snowfall data from the file
    snowfall_data = []
    with open(t, 'r') as file:
        for line in file:
            snowfall_data.append(int(line.strip()))

    # generate ranges by dividing max snowfall by 10 and adding 1
    ranges = [0] * (max(snowfall_data) // 10 + 1)
    for snowfall in snowfall_data:
        index = snowfall // 10
        ranges[index] += 1

    # Plotting the bar chart
    plt.bar([f"{i*10}-{(i+1)*10-1}cms" for i in range(len(ranges))], ranges) 
    plt.xlabel('Snowfall Range (in cms)')
    plt.ylabel('Frequency')
    plt.title('Snowfall Distribution')
    plt.show()

# Test the function
snowfall_file = 'snowfall_data.txt'  # Replace with the actual file path
graphSnowfall(snowfall_file)
