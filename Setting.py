# -*- coding:utf-8 -*-
# Author:Alfred

from cocos.menu import *
from cocos.scene import *
from cocos.layer import *
from cocos.director import *
from cocos.sprite import *
from cocos.audio.effect import Effect


# 创建新的背景层
class BackGroud_seting(Layer):

    def __init__(self):
        super(BackGroud_seting, self).__init__()

        # 获取窗口的宽高
        self.width ,self.height = director.get_window_size()

        # 创建两个背景精灵
        backgroud = Sprite('images/setting-bg.png')
        backgroud.position = self.width // 2, self.height // 2

        # 添加进背景
        self.add(backgroud,0)

        # 创建两个开关精灵
        on = Sprite('images/on.png')
        on.position = 818, 280
        self.add(on, 0)
        on = Sprite('images/on.png')
        on.position = 818, 420
        self.add(on, 0)

# 自定义MainMenu层类
class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__()

        # 创建菜单字体
        self.font_item['font_size'] = 160
        self.font_item['color'] = (255, 255, 255, 255)
        self.font_item_selected['font_size'] = 160
        self.font_item_selected['color'] = (230, 230, 230, 255)

        # 设置菜单项
        on_up = ImageMenuItem('images/ok-up.png', self.on_on_up_callback)

        # 创建菜单
        self.create_menu([on_up], layout_strategy=fixedPositionMenuLayout([(560,130)]))

    def on_on_up_callback(self):
        effect = Effect('sound/Blip.wav')
        effect.play()
        director.pop()



def create_scene():
    # 创建一个场景，并将新的层实例添加到场景中
    main_scene = Scene(BackGroud_seting())
    main_scene.add(MainMenu())

    return main_scene
