import os,shutil

# i = int(input("Enter Start Number: "))
# j = int(input("Enter End Number: "))
#
# while i <= j:
#     s=os.mkdir(str(i))
#
#     os.chdir(os.path.dirname(__file__))
#     k=os.getcwd()
#     print(k)
#     with open(f'{k}\{str(i)}\{str(i)}.txt', 'w') as f:
#         print(f)
#
#
#
#     i += 1

'''
create multiple folders with multiple files
'''

# for i in range(1,11):
#     s = os.mkdir(str(i))
#     for j in range(1,16):
#         k = os.getcwd()
#         with open(f'{k}\{str(i)}\{str(j)}.txt', 'w') as f:
#             f.write("Woops! I have deleted the content!")


"""
delete multiple folders with multiple lines 
"""


for i in range(1,11):
    shutil.rmtree(str(i))


