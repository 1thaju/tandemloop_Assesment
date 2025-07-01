def generate_odd_series_problem2(a: int):
    if a < 1:
        return "Input must be a positive integer."
    
    series = []
    for i in range(a):
        series.append(2 * i + 1)
    return ", ".join(map(str, series))

if __name__ == "__main__":
    # Example Usage
    print(f"Input a = 1, then output : {generate_odd_series_problem2(1)}")
    print(f"Input a = 2, then output : {generate_odd_series_problem2(2)}")
    print(f"Input a = 3, then output : {generate_odd_series_problem2(3)}")
    print(f"Input a = 4, then output : {generate_odd_series_problem2(4)}")
    print(f"Input a = 5, then output : {generate_odd_series_problem2(5)}") 