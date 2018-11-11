# -*- coding:utf-8 -*-
# Author:Alfred

from cocos.sprite import *
from cocos.scene import *
from cocos.layer import *

# 自定义场景层类
class BackGroud(Layer):

    def __init__(self):
        super(BackGroud, self).__init__()

        # 获得窗口的宽度和高度
        self.width, self.height = director.get_window_size()

        # 创建背景精灵
        backgroud = Sprite('images/background.png')
        backgroud.position = self.width // 2, self.height // 2

        # 将背景添加到层中
        self.add(backgroud, -1)

        # 创建山和树以及人等精灵
        mountain1 = Sprite('images/mountain1.png',scale=0.6)
        mountain1.position = 360,500
        self.add(mountain1, 1)

        mountain2 = Sprite('images/mountain2.png', scale=0.6)
        mountain2.position = 800, 500
        self.add(mountain2, 1)

        tree = Sprite('images/tree.png', scale=0.6)
        tree.position = 360, 200
        self.add(tree, 1)

        hero = Sprite('images/hero.png', scale=0.6)
        hero.position = 800, 200
        self.add(hero, 1)



if __name__ == "__main__":
    # 初始化导演，设置窗口的高、宽、标题
    director.init(width=1136, height=640, caption="Hello World")

    # 创建HelloWorld层实例
    hello_layer = BackGroud()

    # 创建一个场景，并将HelloWorld层实例添加到场景中
    main_scene = Scene(hello_layer)

    # 开始启动main_scene场景
    director.run(main_scene)
