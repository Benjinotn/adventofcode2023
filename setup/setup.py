import os

root_dir = os.path.normpath(os.getcwd() + os.sep + os.pardir)

os.chdir(root_dir)

for day in range(1, 26):
    dir_to_add = root_dir + "\day" + str(day)
    file_to_add = dir_to_add + "\day" + str(day) + ".py"
    print(file_to_add)
    print(dir_to_add)

    if not os.path.exists(dir_to_add):
        print(dir_to_add , "Created")
        os.mkdir(dir_to_add)
    else:
        print("Folder already exists, skipping creation")

    try:
        fp = open(file_to_add, 'x')
        fp.close()
    except FileExistsError:
        print("File already exists, skipping creation")
        



