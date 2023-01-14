import numpy as np
import sys

"""
read the file and return a list of data inside the file

args:
    file_name (str): a name of the file

returns:
    list: a list of data inside the file
"""
def get_data(file_name):
    with open(file_name, 'r') as file:
        return list(map(float, file))

"""
print the statistics summary of a data list if it is not empty; otherwise, print error message

args:
    data (list): a list of numerical data
"""
def print_stat(data):
    if (not data):
        print('[ERROR]: data list is empty')
        return
    print(f'mean: {np.mean(data)} std: {np.std(data)} min: {np.min(data)} max {np.max(data)} n: {len(data)}')

"""
put everything together and start the program
"""
def main():
    # get file names
    files = sys.argv[1:]
    # check if any file name is given
    if (not files):
        print('[ERROR]: please enter a file name')
    else:
        try:
            combined = []
            for file in files:
                data = get_data(file)
                print(file)
                print_stat(data)
                combined += data
            print('combined')
            print_stat(combined)
        except Exception as e:
            print('[ERROR]:', e)

if __name__ == '__main__':
    main()
