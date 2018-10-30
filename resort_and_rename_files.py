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
        os.rename(file_list_dir[index], to_rename_dir)


def rename_pics(file_dir, from_tag=0, prefix='', suffix='_'):
    file_list = get_file_names(file_dir, {'.jpg', '.JPG'})
    rename_file(file_list, from_tag=from_tag, prefix=prefix, suffix=suffix)


def rename_models(file_dir, from_tag=0, prefix='', suffix='_'):
    file_list = get_file_names(file_dir, {'.psd', '.tif'})
    rename_file(file_list, from_tag=from_tag, prefix=prefix, suffix=suffix)


def de_rename(file_dir):
    # file_list = os.listdir(file_dir)
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            orgin_file = os.path.join(root, file)
            print('orgin_name:', orgin_file)
            strs = os.path.splitext(file)
            name2 = strs[0]
            if name2[2] == "_":
                new_name = name2[3:] + strs[1]
                rename_to_file = os.path.join(root, new_name)
                print('rename to: ' + rename_to_file)
                os.rename(orgin_file, rename_to_file)




if __name__ == "__main__":
    folder_path = r'E:\temp\生日迎宾牌模板'
    rename_pics(folder_path, 1, prefix="EH")
    rename_models(folder_path, 1, prefix="EH")
    # rename_pics(r'D:\temp\temp2', 31)
    # de_rename(folder_path)