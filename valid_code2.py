# -*- coding: utf-8 -*-
# author: luo xu
# create time: 2020/9/24 16:51
import random
import base64

from PIL import Image, ImageDraw, ImageFont, ImageFilter


class ValidCode(object):
    __isNoise = True  # 是否画干扰点

    __str = None  # 自定义验证码字符集
    __type = 2  # 验证码类型 1、纯字母  2、数字字母混合
    __ttfPath = "./1.ttf"

    def __init__(self, length=4, size=80):

        self.__length = length  # 验证码长度
        self.__fontSize = size  # 验证码大小
        self.__width = self.__fontSize * self.__length  # 图片宽度
        self.__height = int(self.__fontSize * 1.5)  # 图片高度

    def get_code_image(self):
        # 创建随机验证码
        self.create_code()
        # 创建画布
        self.create_image()
        # 添加干扰点
        self.create_noise()

        self.print_string()
        # 模糊处理
        self.create_filter()

        self.__img.show()

    def create_filter(self):
        self.__img = self.__img.filter(ImageFilter.BLUR)
        filters = ImageFilter.ModeFilter(7)
        self.__img = self.__img.filter(filters)

    def print_string(self):
        font = ImageFont.truetype(self.__ttfPath, self.__fontSize)
        for i in range(self.__length):
            color = (random.randint(30, 150), random.randint(30, 150), random.randint(30, 150))
            x = random.uniform(self.__fontSize * i * 0.95, self.__fontSize * i * 1.1)
            y = self.__fontSize * random.uniform(0.3, 0.5)
            self.__draw.text((x, y), self.__code[i], font=font, fill=color)

    def create_noise(self):
        if not self.__isNoise:
            return
        font = ImageFont.truetype(font=self.__ttfPath, size=int(self.__fontSize / 1.8))
        for i in range(5):
            noise_color = (random.randint(150, 190), random.randint(150, 190), random.randint(150, 190))
            put_str = random.sample(self.__str, 2)
            for j in range(2):
                size = (random.randint(-10, self.__width), random.randint(-10, self.__height))
                self.__draw.text(size, put_str[j], font=font, fill=noise_color)

    def create_image(self):
        # 设置浅色背景
        bg_color = (random.randint(190, 255), random.randint(190, 255), random.randint(190, 255))
        # 生成幕布
        self.__img = Image.new("RGB", (self.__width, self.__height), color=bg_color)
        # 加载画笔
        self.__draw = ImageDraw.Draw(self.__img)

    def create_code(self):
        '''创建验证码字符'''
        if not self.__str:
            number = '123456789'
            str_upper = ''.join(chr(x) for x in range(65, 91))
            str_lower = str_upper.lower()
            if self.__type == 1:
                self.__str = number
            else:
                self.__str = number + str_upper + str_lower
        self.__code = random.sample(self.__str, self.__length)

    def get_code_image_base64(self):
        pass


if __name__ == '__main__':
    vc = ValidCode()
    vc.get_code_image()
