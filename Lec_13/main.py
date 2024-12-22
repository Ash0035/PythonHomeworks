import random
import time
from threading import Thread
from multiprocessing import Process,Manager

words = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"]

def generate_random_word():
    return random.choice(words)

def generate_random_sentence(sentence_length):
    return ' '.join(random.choices(words, k=sentence_length))


def sequential_word_count(file_path):
    count_word = {}
    with open(file_path, 'r') as file:
        content = file.read().lower()
        word_list = content.split()
        for word in word_list:
            if word in count_word:
                count_word[word] += 1
            else:
                count_word[word] = 1
    return count_word


def multithreaded_word_count(file_path, num_threads=4):
    def thread_worker(chunk, result):
        try:
            local_count = {}
            words = chunk.split()
            for word in words:
                if word in local_count:
                    local_count[word] += 1
                else:
                    local_count[word] = 1
            result.append(local_count)
        except Exception as e:
            print(f"Error in thread worker: {e}")

    with open(file_path, 'r') as file:
        content = file.read()

    chunk_size = len(content) // num_threads
    threads = []
    results = []  

    for i in range(num_threads):
        start = i * chunk_size
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        chunk = content[start:end]
        thread = Thread(target=thread_worker, args=(chunk, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_count = {}
    for local_count in results:
        for word, count in local_count.items():
            final_count[word] = final_count.get(word, 0) + count

    return final_count



def process_worker(chunk, result_list):
    local_count = {}
    words = chunk.split()
    for word in words:
        if word in local_count:
            local_count[word] += 1
        else:
            local_count[word] = 1
    result_list.append(local_count)


def multiprocessing_word_count(file_path, num_processes=4):
    with open(file_path, 'r') as file:
        content = file.read()

    chunk_size = len(content) // num_processes
    manager = Manager()
    results = manager.list()  

    processes = []
    for i in range(num_processes):
        start = i * chunk_size
        end = None if i == num_processes - 1 else (i + 1) * chunk_size
        chunk = content[start:end]
        process = Process(target=process_worker, args=(chunk, results))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

 
    final_count = {}
    for local_count in results:
        for word, count in local_count.items():
            final_count[word] = final_count.get(word, 0) + count

    return final_count




def compare_word_count_methods(file_path):

    start_time = time.time()
    sequential_count = sequential_word_count(file_path)
    sequential_time = time.time() - start_time
    print(f"Sequential time: {sequential_time:.4f} seconds")

    start_time = time.time()
    multithreaded_count = multithreaded_word_count(file_path)
    multithreading_time = time.time() - start_time
    print(f"Multithreading time: {multithreading_time:.4f} seconds")

 
    start_time = time.time()
    multiprocessing_count = multiprocessing_word_count(file_path)
    multiprocessing_time = time.time() - start_time
    print(f"Multiprocessing time: {multiprocessing_time:.4f} seconds")


    if multithreading_time > 0:
        multithreading_speedup = sequential_time / multithreading_time
        print(f"Multithreading Speedup: {multithreading_speedup:.2f}x")
    else:
        print("Multithreading Speedup: Division by zero occurred!")

    if multiprocessing_time > 0:
        multiprocessing_speedup = sequential_time / multiprocessing_time
        print(f"Multiprocessing Speedup: {multiprocessing_speedup:.2f}x")
    else:
        print("Multiprocessing Speedup: Division by zero occurred!")

    print("\nExecution Times (seconds):")
    print(f"Sequential: {sequential_time:.4f}")
    print(f"Multithreading: {multithreading_time:.4f}")
    print(f"Multiprocessing: {multiprocessing_time:.4f}")







if __name__=="__main__":

 file_path = input("Enter the file path: ")
 with open(file_path, 'w') as file:
   
    for _ in range(100000):
        random_word = generate_random_word()  
        file.write(random_word + '\n')  

    for _ in range(10000):
        sentence = generate_random_sentence(10)  
        file.write(sentence + '\n') 
      
 print(sequential_word_count(file_path))
 compare_word_count_methods(file_path)
