from PIL import Image, ImageDraw
import my_calculate
import my_draw
import resort_and_rename_files
import os
import cv2


if __name__ == "__main__":
    # 横向，纵向各多少张照片
    h_pic_count = 1
    v_pic_count = 3

    my_calculate.set_model_ratio(90/60)
    my_calculate.set_pic_count_in_horizontal(h_pic_count)
    my_calculate.set_pic_count_in_vertical(v_pic_count)
    my_calculate.run1()
    img_width = my_calculate.get_pic_width()
    img_height = my_calculate.get_pic_height()
    model_width = my_calculate.get_model_width()
    model_height = my_calculate.get_model_height()
    models_pos = my_calculate.get_models_pos()
    im = Image.new("RGBA", (img_width, img_height), "black")

    # im2 = Image.open(r"D:\PSproj\客户图\2018年8月8日_主人的小白狐\2018年8月6日_ppzhong93_003.jpg")
    # im3 = im2.resize((model_width, model_height), Image.ANTIALIAS).convert("RGBA")

    # im.paste(im3, (0, 0, model_width, model_height), im3)

    # pos = models_pos[0]
    # my_draw.bm(im, pos, im3)
    # my_draw.model(im, pos, im3, "11")
    # my_draw.model(im, pos, im3, "22")
    # my_draw.model(im, pos, im3, "33")

    # for pos in models_pos:
    #     my_draw.model(im, pos, im3, "11")

    # im.show()

    prefix = "结婚迎宾牌模板"
    file_path = r'D:\temp\结婚迎宾牌模板'
    file_path = r'E:\temp\生日迎宾牌模板\新建文件夹'
    new_file_path = file_path + '缩略图'
    if not os.path.exists(new_file_path):
        os.makedirs(new_file_path)

    files = resort_and_rename_files.get_file_names(file_path, {'.jpg', '.JPG'})

    pic_count = h_pic_count * v_pic_count

    for i in range(0, len(files), pic_count):
        file_group = files[i: i + pic_count]
        print(file_group)
        im = Image.new("RGBA", (img_width, img_height), "black")
        tag_temp = []
        for file, pos in zip(file_group, models_pos):

            # Image 的缩放方式
            im2 = Image.open(file)
            im3 = im2.resize((model_width, model_height), Image.ANTIALIAS).convert("RGBA")

            # opencv的缩放
            # crop_size = (model_width, model_height)
            # im2 = cv2.imread(file)
            # im3 = cv2.resize(im2, crop_size)

            tag = os.path.split(file)[1].split('_')[0]
            tag_temp.append(tag)
            my_draw.model2(im, pos, im3, tag)
        # im.show()
        name = prefix + "_" + tag_temp[0] + "-" + tag_temp[pic_count - 1]
        path = new_file_path + "\\" + name + '.jpg'

        im4 = im.convert("RGB")
        my_draw.save(im4, path)
        print(path)



