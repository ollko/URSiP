import sys
from controller import (
	insert_to_database,
	read_and_process_data
)
 

def get_file_name():
	print("Enter the file name:")
	return sys.stdin.readline().strip()


def main():
	file_name = get_file_name()
	data = read_and_process_data(file_name)
	insert_to_database(data)


if __name__=="__main__":
	main()
