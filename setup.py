import os
from utils import *

root_dir = os.getcwd()

variables = get_variables()

year = variables["year"]


for day in range(1, 26):
    dir_to_add = root_dir + "\day" + str(day)
    file_to_add = dir_to_add + "\day" + str(day) + ".py"

    if not os.path.exists(dir_to_add):
        os.mkdir(dir_to_add)
        print(dir_to_add , "Created")
    else:
        print("folder: day{} already exists, skipping creation".format(day))

    try:
        fp = open(file_to_add, 'x')
        print(file_to_add, "Created")

        fp.write("import sys\n")
        fp.write("import os\n")
        fp.write("sys.path.append(\"../\")\n")
        fp.write("from utils import *\n\n")

        fp.write("file = \"day_{}.txt\"\n".format(day))
        fp.write("if not os.path.isfile(file):\n")
        fp.write("\tprint(\"fetching text input\")\n")
        fp.write("\ttext_file = open(file, \"w\")\n")
        fp.write("\tos.chdir(\"../\")\n")
        fp.write("\tdata = get_puzzle_input_from_web(day={})\n".format(day))
        fp.write("\ttext_file.write(str(data))\n")
        fp.write("\ttext_file.close()\n")
        fp.write("else:\n")
        fp.write("\tprint(\"file already exists, skipping web scrape\")\n")
        fp.write("\tdata = get_text_input_from_file(file)\n")

        fp.close()
    except FileExistsError:
        print("file: day{}.py already exists, skipping creation".format(day))
    
    print("\n")


        



