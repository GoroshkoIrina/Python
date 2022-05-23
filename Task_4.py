import os


def get_file_name(fname):
    return os.path.join("some_data", fname)

result_dict = {}
for file_item in os.listdir("some_data"):
    if os.path.isfile(get_file_name(file_item)):
        file_size = os.stat(get_file_name(file_item)).st_size
        size_rank = 10 ** (len(str(file_size)))
        if result_dict.get(size_rank):
            result_dict[size_rank] = result_dict[size_rank] + 1
        else:
            result_dict[size_rank] = 1
print(result_dict)
