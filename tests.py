from functions.get_files_info import *
from functions.get_file_content import *
from functions.write_file import *

# # print ("1. -------------------------")
# get_files_info("calculator", ".")
# # print ("2. -------------------------")
# get_files_info("calculator", "pkg")
# # print ("3. -------------------------")
# get_files_info("calculator", "/bin")
# # print ("4. -------------------------")
# get_files_info("calculator", "../")

# get_file_content("calculator", "lorem.txt")

# print ("1. -------------------------")
# get_file_content("calculator", "main.py")
# print ("2. -------------------------")
# get_file_content("calculator", "pkg/calculator.py")
# print ("3. -------------------------")
# get_file_content("calculator", "/bin/cat")
# print ("4. -------------------------")
# get_file_content("calculator", "pkg/does_not_exist.py")

write_tests = [
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed"),
]

def test_printer(file_func, tests):
    count = 1
    for test in tests:
        print (f"'{count}'. -------------------------")
        print(file_func(*test))
        count += 1

test_printer(write_file, write_tests)