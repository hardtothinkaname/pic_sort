import os


def get_file_names(file_dir, types):
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] in types:
                file_list.append(os.path.join(root, file))
    return file_list


def rename_file(file_list_dir, from_tag=0, prefix='', suffix='_'):
    for index in range(len(file_list_dir)):
        split = os.path.split(file_list_dir[index])
        print('orgin_name:', file_list_dir[index])
        num = from_tag + index
        num = str(num).zfill(2)
        rename_to = prefix + num + suffix + split[1]
        to_rename_dir = split[0] + '\\' + rename_to
        print('rename to:', to_rename_dir)
        # os.rename(file_list_dir[index], to_rename_dir)


def rename_pics(file_dir, from_tag=0):
    file_list = get_file_names(file_dir, {'.jpg'})
    rename_file(file_list, from_tag=from_tag)


def rename_models(file_dir, from_tag=0):
    file_list = get_file_names(file_dir, {'.psd', '.tif'})
    rename_file(file_list, from_tag=from_tag)



if __name__ == "__main__":
    rename_pics(r'D:\temp\新结婚迎宾牌 - 副本', 31)
    rename_models(r'D:\temp\新结婚迎宾牌 - 副本', 31)
    # rename_pics(r'D:\temp\temp2', 31)