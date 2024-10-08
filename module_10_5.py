import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())

start=datetime.datetime.now()
filenames = [f'./file {number}.txt' for number in range(1, 5)]
end=datetime.datetime.now()
print(end-start)

"""
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
        all_data=[]
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
start = datetime.datetime.now()
end = datetime.datetime.now()
print(end-start)"""


