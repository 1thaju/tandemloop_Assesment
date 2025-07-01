def count_multiples(input_list: list):
    multiples_count = {i: 0 for i in range(1, 10)}

    for num in input_list:
        for i in range(1, 10):
            if num % i == 0:
                multiples_count[i] += 1
    return multiples_count

if __name__ == "__main__":
    # Example Usage
    input_data = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    output = count_multiples(input_data)
    print(f"Input: {input_data}")
    print(f"Output: {output}")

    input_data_2 = [7, 14, 21]
    output_2 = count_multiples(input_data_2)
    print(f"Input: {input_data_2}")
    print(f"Output: {output_2}") 