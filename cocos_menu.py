# -*- coding:utf-8 -*-
# Author:Alfred
from cocos.menu import *
from cocos.scene import *
from cocos.layer import *

# 自定义MainMenu层类
class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__()

        # 创建菜单字体
        self.font_item['font_size'] = 32
        self.font_item_selected['font_size'] = 40

        # 设置菜单项
        item1 = MenuItem('开始',self.on_menuitem1_callback)
        item2 = ToggleMenuItem('音效', self.on_menuitem2_callback,False)

        # 创建菜单
        self.create_menu([item1,item2],selected_effect=shake(),
                         unselected_effect=shake_back())

    def on_menuitem1_callback(self):
        print("call on_menuitem1_callback")

    def on_menuitem2_callback(self,value):
        print("call on_menuitem2_callback",value)

if __name__ == "__main__":
    # 初始化导演
    director.init(caption="example menu")

    # 创建主菜单
    main_menu = MainMenu()

    # 创建一个场景，并将HelloWorld层实例添加到场景中
    main_scene = Scene(main_menu)

    # 开始启动main_scene场景
    director.run(main_scene)
