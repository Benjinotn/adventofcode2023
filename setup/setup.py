import os

root_dir = os.path.normpath(os.getcwd() + os.sep + os.pardir)

os.chdir(root_dir)

for day in range(1, 26):
    dir_to_add = root_dir + "\day" + str(day)

    print(dir_to_add)

    os.mkdir(dir_to_add)

