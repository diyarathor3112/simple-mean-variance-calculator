import math

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_variance(data, mean):
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_std(variance):
    return math.sqrt(variance)

def main():
    data = list(map(float, input("Enter numbers separated by space: ").split()))
    
    mean = calculate_mean(data)
    variance = calculate_variance(data, mean)
    std_dev = calculate_std(variance)
    
    print("\n--- Results ---")
    print(f"Mean: {mean:.4f}")
    print(f"Variance: {variance:.4f}")
    print(f"Standard Deviation: {std_dev:.4f}")

main()
