# -*- coding:utf-8 -*-
# Author:Alfred

from cocos.sprite import *
from cocos.menu import *
from cocos.scene import *
from cocos.layer import *
from cocos.director import *

# 自定义gamelayer
class GameBackGroud(Layer):

    def __init__(self):
        super().__init__()

        # 获取屏幕尺寸
        s_width,s_height = director.get_window_size()

        # 创建精灵
        background = Sprite('images/game-bg.png')
        background.position = s_width//2,s_height//2

        # 添加精灵
        self.add(background)

# 自定义HelloWorld层类
class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__()

        # 创建菜单字体
        self.font_item['font_size'] = 100
        self.font_item['color'] = (23,233,21,255)
        self.font_item_selected['font_size'] = 140
        self.font_item_selected['color'] = (123, 133, 231, 255)

        # 设置图片菜单项
        start_item = ImageMenuItem('images/start-up.png',self.on_start_item_callback)
        set_item = ImageMenuItem('images/setting-up.png', self.on_set_item_callback)
        help_item = ImageMenuItem('images/help-up.png', self.on_help_item_callback)


        # 创建菜单
        self.create_menu([start_item,set_item,help_item],
                         layout_strategy=fixedPositionMenuLayout(
                             [(800,480),(480,370),(1000,250)]
                         ))

    def on_start_item_callback(self):
        print("call on_start_item_callback")

    def on_set_item_callback(self):
        print("call on_set_item_callback")

    def on_help_item_callback(self):
        print("call on_help_item_callback")

if __name__ == "__main__":
    # 初始化导演
    director.init(width=1200, height=680,caption="example photo menu")

    # 创建一个场景，并将HelloWorld层实例添加到场景中
    main_scene = Scene(GameBackGroud())

    # 创建主菜单
    main_scene.add(MainMenu())

    # 开始启动main_scene场景
    director.run(main_scene)
