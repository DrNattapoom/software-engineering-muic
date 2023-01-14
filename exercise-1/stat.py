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
    print('Statistics Summary')
    print('mean:', np.mean(data))
    print('std:', np.std(data))
    print('min:', np.min(data))
    print('max:', np.max(data))

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
            for file in files:
                data = get_data(file)
                print_stat(data)
        except Exception as e:
            print('[ERROR]:', e)

if __name__ == '__main__':
    main()
