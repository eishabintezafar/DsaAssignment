from typing import List

def multiply_by_two(digits: List[int]) -> List[int]:
    result = []
    carry = 0
    
    # Start from the least significant digit and move left
    for i in range(len(digits) - 1, -1, -1):
        product = digits[i] * 2 + carry
        result.insert(0, product % 10)  # Add the last digit of the product
        carry = product // 10  # Carry the remaining part
    
    if carry > 0:
        result.insert(0, carry)  # Add remaining carry if any
    
    return result

# Main function to test the functionality
if __name__ == "__main__":
    # Test Case 1
    input1 = [2, 3, 4]
    print("Input:", input1)
    print("Output:", multiply_by_two(input1))
    
    # Test Case 2
    input2 = [0]
    print("Input:", input2)
    print("Output:", multiply_by_two(input2))
    
    # Test Case 3
    input3 = [5, 0, 0]
    print("Input:", input3)
    print("Output:", multiply_by_two(input3))
