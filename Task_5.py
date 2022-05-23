import os


def get_file_name(fname):
    return os.path.join("some_data", fname)

result_dict = {}
for file_item in os.listdir("some_data"):
    if os.path.isfile(get_file_name(file_item)):
        ext = file_item.rsplit('.', maxsplit=1)[-1].lower()
        file_size = os.stat(get_file_name(file_item)).st_size
        size_rank = 10 ** (len(str(file_size)))
        if result_dict.get(size_rank):
            tuple_old = result_dict.pop(size_rank)
            count = tuple_old[0]
            ext_set = tuple_old[1]
            ext_set.add(ext)
            result_dict[size_rank] = (count + 1, ext_set)
        else:
            result_dict[size_rank] = (1, {ext})
print(result_dict)
