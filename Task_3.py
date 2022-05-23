import os
import shutil


def create_dirs(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

for item in os.walk("my_project"):
    dir_name = item[0]
    subfolder_list = item[1]
    file_name_list = item[2]

    if not (dir_name.find('templates') == -1):
        for subfolder_name in subfolder_list:
            create_dirs(os.path.join("my_project\\templates", dir_name[dir_name.rfind("templates") + 10::], subfolder_name))

        for file_name in file_name_list:
            shutil.copy(os.path.join(dir_name, file_name), os.path.join("my_project\\templates", dir_name[dir_name.rfind("templates")+10::]))
