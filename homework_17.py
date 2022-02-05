import sys
import os
cwd = os.getcwd()
file_path = os.path.join(cwd, "sample.txt")

# 1
# lines_sum = sum(1 for line in open("sample.txt"))
#
# all_num = 0
# cycle = 1
#
# with open("sample.txt") as file:
#     file = file.read()

# while range(0, lines_sum):
#     num = 0
#     for i in file:
#         if i.isdigit():
#             num += 1
#         elif i == "\n":
#             print("Line {} = {} number".format(cycle, num))
#             all_num += num
#             num = 0
#             cycle += 1
#
#         lines_sum -= 1
#
# print("In file, {} number".format(all_num))

# 2
# lines_sum = sum(1 for line in open("sample.txt"))
# count = 0
# cycle = 1
#
# with open("sample.txt") as file:
#     file = file.read()
#
# cipher = input("Enter the num: ")
#
# if cipher.isdigit():
#     num = int(cipher)
# else:
#     print("Wrong value!")
#     sys.exit()
#
# while range(0, lines_sum):
#     num = 0
#     for i in file:
#         if i.isdigit() and i == cipher:
#             num += 1
#         elif i == "\n":
#             count += num
#             num = 0
#             cycle += 1
#
#         lines_sum -= 1
#
# print("Cipher {} repeats in the text {} times".format(cipher, count))


# 4
with open("sample.txt") as f:
    with open("sample_2.txt", "w") as f1:
        for line in f:
            for i in line:
                if i.isalpha():
                    f1.write(i)
