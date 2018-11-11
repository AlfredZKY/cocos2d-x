# -*- coding:utf-8 -*-
# Author:Alfred

from cocos.menu import *
from cocos.scene import *
from cocos.director import *
from cocos.sprite import *
from cocos.layer.util_layers import ColorLayer
from cocos.actions import *

# 创建一个全局变量
hero = None


# 创建一个自定义的背景层
class BackGroud(ColorLayer):

    def __init__(self):
        super(BackGroud, self).__init__(255, 255, 255, 255)

        # 获取窗口的大小
        self.width, self.height = director.get_window_size()
        global hero

        hero = Sprite('images/hero.png')
        hero.position = 560, 320

        # 把精灵添加进层
        self.add(hero)


# 自定义MainMenu层类
class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__()

        # 创建菜单字体，颜色,及选中字体时的颜色
        self.font_item['font_size'] = 20
        self.font_item['color'] = (0, 0, 0, 255)
        self.font_item_selected['font_size'] = 26
        self.font_item_selected['color'] = (0, 0, 0, 255)

        # 设置图片项
        item1 = MenuItem('顺序', self.on_order_callback)
        item2 = MenuItem('并列', self.on_tied_callback)
        item3 = MenuItem('有限次数重复', self.on_times_callback)
        item4 = MenuItem('无限次数重复', self.on_notimes_callback)

        x = 120
        y = 480
        step = 50

        # 创建菜单
        self.create_menu([item1, item2, item3, item4],
                         layout_strategy=fixedPositionMenuLayout(
                             [(x, y),
                              (x, y - step),
                              (x, y - step * 2),
                              (x, y - step * 3)
                              ]
                         ))

    def on_order_callback(self):
        print("call on_order_callback")
        act1 = Place((500,200))
        act2 = MoveBy((130, 320), duration=2)
        act3 = JumpBy((80,100), height=30, jumps=4, duration=3)
        action = act1 + act2 + act3
        hero.do(action)

    def on_tied_callback(self):
        print("call on_tied_callback")
        act1 = MoveTo((500,450), 2)
        act2 = RotateTo(40,2)
        action = act1 | act2
        hero.do(action)

    def on_times_callback(self):
        print("call on_times_callback")
        act = JumpBy((30, 30), height=30, jumps=5, duration=2)
        act = act * 3
        hero.do(act)

    def on_notimes_callback(self):
        print("call on_notimes_callback")
        act1 = RotateBy(40, 2)
        action = Repeat(act1)
        hero.do(action)


if __name__ == "__main__":
    # 初始化导演
    director.init(width=1136, height=640, caption="间隔动作")

    # 创建一个场景，并将HelloWorld层实例添加到场景中
    main_scene = Scene(BackGroud())
    main_scene.add(MainMenu())

    # 开始启动main_scene场景
    director.run(main_scene)
