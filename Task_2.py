import os


def create_dirs(dir_path):
    #создание вложенных папок
    #dir_path = os.path.join('data', 'src')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def create_file(file_name):
    #создание пустого файла
    open(file_name, 'w').close()

def create_starter(config_file_name):
    catalog_list = []
    with open(config_file_name, 'r', encoding='utf-8') as f_config:
        last_dir = []
        last_rank = 0
        for line in f_config:
            parent_path =""
            #файл или папка? если есть точка
            name = line[line.rfind('-')+1::].strip()
            if name.count('.'):
                el_type = "file"
            else:
                el_type = "dir"
            rank = line.rfind('-') // 3

            if rank >= last_rank and rank:
                for str_dir in last_dir:
                    parent_path += str_dir + "\\"

            if rank < last_rank:
                for i in range(last_rank - rank):
                    last_dir.pop()
                for str_dir in last_dir:
                    parent_path += str_dir + "\\"

            print(rank, " ", parent_path, name," ", el_type, sep="")
            catalog_list.append([parent_path + name, el_type])

            if el_type == "dir":
                last_dir.append(name)
            last_rank = rank
    return catalog_list


for elem in create_starter('config.yaml'):
    if elem[1] == "dir":
        create_dirs(elem[0])
    if elem[1] == "file":
        create_file(elem[0])
