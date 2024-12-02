import random
import time

def generate_file(filename):
    with open(filename, 'w') as file:
        for _ in range(100):
            line = ' '.join(str(random.randint(1, 100)) for _ in range(20))
            file.write(line + '\n')

def read_and_convert_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield list(map(int, line.split()))

def filter_numbers(numbers):
    return list(filter(lambda x: x > 40, numbers))

def write_filtered_data(filename, filtered_data):
    with open(filename, 'w') as file:
        for line in filtered_data:
            file.write(' '.join(map(str, line)) + '\n')

def read_file_as_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield list(map(int, line.split()))

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@measure_time
def process_file(filename):
    converted_lines = read_and_convert_file(filename)
    filtered_data = [filter_numbers(line) for line in converted_lines]
    write_filtered_data(filename, filtered_data)

if __name__ == "__main__":
    filename = 'main.txt'
    generate_file(filename)
    process_file(filename)
    
    print("Reading filtered data from the file as a generator:")
    for i, line in enumerate(read_file_as_generator(filename)):
        print(line)
        if i >= 5:
            break
