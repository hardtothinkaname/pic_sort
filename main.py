from PIL import Image, ImageDraw
import my_calculate
import my_draw


if __name__ == "__main__":
    my_calculate.set_pic_count_in_horizontal(3)
    my_calculate.run1()
    img_width = my_calculate.get_pic_width()
    img_height = my_calculate.get_pic_height()
    model_width = my_calculate.get_model_width()
    model_height = my_calculate.get_model_height()
    models_pos = my_calculate.get_models_pos()
    im = Image.new("RGBA", (img_width, img_height), "black")

    im2 = Image.open(r"D:\PSproj\客户图\2018年8月8日_主人的小白狐\2018年8月6日_ppzhong93_003.jpg")
    im3 = im2.resize((model_width, model_height), Image.ANTIALIAS).convert("RGBA")

    # im.paste(im3, (0, 0, model_width, model_height), im3)

    # pos = models_pos[0]
    # my_draw.bm(im, pos, im3)
    # my_draw.model(im, pos, im3, "11")
    # my_draw.model(im, pos, im3, "22")
    # my_draw.model(im, pos, im3, "33")

    for pos in models_pos:
        my_draw.model(im, pos, im3, "11")



    im.show()



