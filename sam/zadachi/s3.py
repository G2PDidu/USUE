import time
import datetime

def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

start = time.time()
for _ in range(5):
    current_time = get_time()
    print(current_time)
    time.sleep(1)
    elapsed_time = time.time() - start
print("Программа выполнялась", elapsed_time, "секунд")