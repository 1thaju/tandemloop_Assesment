def generate_odd_series_problem3(a: int):
    if a < 1:
        return "Input must be a positive integer."
    
    series = []
    num_terms = a if a % 2 != 0 else a - 1
    
    for i in range(num_terms):
        series.append(2 * i + 1)
    return ", ".join(map(str, series))

if __name__ == "__main__":
    # Example Usage
    print(f"Input a = 1, then output : {generate_odd_series_problem3(1)}")
    print(f"Input a = 2, then output : {generate_odd_series_problem3(2)}")
    print(f"Input a = 3, then output : {generate_odd_series_problem3(3)}")
    print(f"Input a = 4, then output : {generate_odd_series_problem3(4)}")
    print(f"Input a = 5, then output : {generate_odd_series_problem3(5)}")
    print(f"Input a = 6, then output : {generate_odd_series_problem3(6)}") 