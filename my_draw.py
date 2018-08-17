from PIL import Image, ImageDraw, ImageFont

im4 = Image.open("name_tag.png").resize((36, 36), Image.ANTIALIAS)
x, y = im4.size
fontsize = 15
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


def tag(canvas, pos):
    # pos是图标中心
    width, height = im4.size
    pos = (int(pos[0] - width / 2), int(pos[1] - height / 2))
    bm(canvas, pos, im4)


def model(canvas, pos, im, name):
    width, height = im.size
    bm(canvas, pos, im)
    pos2 = (pos[0] + width / 2, pos[1])
    tag(canvas, pos2)
    text(canvas, pos2, name)


def save(im, path):
    im.save(path)

