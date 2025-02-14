from typing import List

def add_one(digits: List[int]) -> List[int]:
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0  # Set current digit to 0 if it's 9
    
    # If all digits were 9, create a new list with an extra digit
    return [1] + digits

# Main function to test the functionality
if __name__ == "__main__":
    # Test Case 1
    input1 = [1, 2, 3]
    print("Input:", input1)
    print("Output:", add_one(input1))
    
    # Test Case 2
    input2 = [9, 9]
    print("Input:", input2)
    print("Output:", add_one(input2))
    
    # Test Case 3
    input3 = [0]
    print("Input:", input3)
    print("Output:", add_one(input3))
    
    # Test Case 4
    input4 = [1, 0, 0, 0]
    print("Input:", input4)
    print("Output:", add_one(input4))
