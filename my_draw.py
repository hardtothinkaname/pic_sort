from PIL import Image, ImageDraw, ImageFont
import ConstValue



im4 = Image.open("name_tag.png").resize((36, 36), Image.ANTIALIAS)
x, y = im4.size
fontsize = 30
font = ImageFont.truetype("arial.ttf", fontsize)



def bm(canvas, pos, bm):
    width, height = bm.size
    x = pos[0]
    y = pos[1]
    canvas.paste(bm, (x, y, x + width, y + height), bm)


def text(canvas, pos, name):
    # pos是文字中心
    draw = ImageDraw.Draw(canvas)
    width, height = draw.textsize(name, font=font)
    pos = (int(pos[0] - width / 2), int(pos[1] - height / 2))
    draw.text(pos, name, font=font)


def text(canvas, pos, name, align_x=ConstValue.ALIGNX.center, align_y=ConstValue.ALIGNY.center):
    # pos是文字中心
    draw = ImageDraw.Draw(canvas)
    width, height = draw.textsize(name, font=font)

    pos_x = 0
    if align_x == ConstValue.ALIGNX.center:
        pos_x = int(pos[0] - width / 2)
    elif align_x == ConstValue.ALIGNX.left:
        pos_x = 0
    elif align_x == ConstValue.ALIGNX.right:
        pos_x = int(pos[0] - width)

    pos_y = 0
    if align_y == ConstValue.ALIGNY.center:
        pos_y = int(pos[1] - height / 2)
    elif align_y == ConstValue.ALIGNY.top:
        pos_y = 0
    elif align_y == ConstValue.ALIGNY.bottom:
        pos_y = int(pos[1] - height - 8)


    # pos = (int(pos[0] - width / 2), int(pos[1] - height / 2))
    pos = (pos_x, pos_y)
    draw.text(pos, name, font=font)



def tag(canvas, pos):
    # pos是图标中心
    width, height = im4.size
    pos = (int(pos[0] - width / 2), int(pos[1] - height / 2))
    bm(canvas, pos, im4)


def model(canvas, pos, im, name):
    # 在模板图的正中上方写文字
    width, height = im.size
    bm(canvas, pos, im)
    pos2 = (pos[0] + width / 2, pos[1])
    tag(canvas, pos2)
    text(canvas, pos2, name)


def model2(canvas, pos, im, name):
    # 在模板图的正中上方写文字
    width, height = im.size
    bm(canvas, pos, im)
    pos2 = (pos[0] + width / 2, pos[1])
    # tag(canvas, pos2)
    text(canvas, pos2, name, align_y=ConstValue.ALIGNY.bottom)


def save(im, path):
    im.save(path)

