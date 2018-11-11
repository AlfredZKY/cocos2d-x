# -*- coding:utf-8 -*-
# Author:Alfred

from cocos import text
from cocos.scene import *
from cocos.layer import *
import pyglet

# 自定义HelloWorld层类
class HelloWorld(Layer):

    #打开事件开关
    is_event_handler = True
    def __init__(self):
        super(HelloWorld, self).__init__()
        # 创建标签
        self.label = text.Label('Hello, World!',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')

        # 获得窗口的宽度和高度
        width, height = director.get_window_size()
        # 设置标签的位置
        self.label.position = width // 2, height // 2

        # 添加标签到HelloWorld层
        self.add(self.label)

    def on_key_press(self,key,modifiers):
        print("on_key_press",key,modifiers)
        if key == pyglet.window.key.SPACE:
            self.label.element.text = 'space press'

    def on_key_release(self, key, modifiers):
        print("on_key_release", key, modifiers)
        if key == pyglet.window.key.SPACE:
            self.label.element.text = 'space release'

if __name__ == "__main__":
    # 初始化导演，设置窗口的高、宽、标题
    director.init(width=640, height=480, caption="Keyboard event")

    # 创建HelloWorld层实例
    hello_layer = HelloWorld()

    # 创建一个场景，并将HelloWorld层实例添加到场景中
    main_scene = Scene(hello_layer)

    # 开始启动main_scene场景
    director.run(main_scene)
