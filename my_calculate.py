


# 输入的参数

# 离图片顶部距离
top_margin = 50

# 离图片底部距离
bottom_margin = 10

# 模板之间的间隔距离
horizontal_margin = 20

# 水平方向放多少张照片
pic_count_in_horizontal = 1

# 垂直方向放多少张照片
pic_count_in_vertical = 1

# 照片的比例
model_ratio = 60 / 160

pic_width = 750

# 输出的结果

pic_height = 0

models_pos = []

model_width = 0
model_height = 0


def set_top_margin(margin=50):
    global top_margin
    top_margin = margin


def set_bottom_margin(margin=50):
    global bottom_margin
    bottom_margin = margin


def set_horizontal_margin(margin=20):
    global horizontal_margin
    horizontal_margin = margin


def set_pic_count_in_horizontal(count=1):
    global pic_count_in_horizontal
    pic_count_in_horizontal = count


def set_pic_count_in_vertical(count=1):
    global pic_count_in_vertical
    pic_count_in_vertical = count


def set_model_ratio(ratio=0.5):
    global model_ratio
    model_ratio = ratio


def set_pic_width( width=750):
    global pic_width
    pic_width = width


def run1():
    global model_width
    global model_height
    global models_pos
    global pic_height
    model_width = (pic_width - (pic_count_in_horizontal + 1) * horizontal_margin) / pic_count_in_horizontal
    model_height = model_width / model_ratio
    pic_height = pic_count_in_vertical * (model_height + top_margin) + bottom_margin

    for j in range(pic_count_in_vertical):
        for i in range(pic_count_in_horizontal):
            pos_x = i * (model_width + horizontal_margin) + horizontal_margin
            pos_y = j * (model_height + top_margin) + top_margin
            models_pos.append((int(pos_x), int(pos_y)))


def get_model_width():
    return int(model_width)


def get_model_height():
    return int(model_height)


def get_pic_height():
    return int(pic_height)


def get_pic_width():
    return int(pic_width)


def get_models_pos():
    return models_pos



if __name__ == "__main__":
    set_top_margin(80)
    set_pic_count_in_horizontal(3)
    run1()
    print(get_model_width())
    print(get_model_height())
    print(get_pic_height())
    print(models_pos)


