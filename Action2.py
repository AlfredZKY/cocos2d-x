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
        MoveTo = MenuItem('MoveTo', self.on_moveto_callback)
        MoveBy = MenuItem('MoveBy', self.on_moveby_callback)
        JumpTo = MenuItem('JumpTo', self.on_jumpto_callback)
        JumpBy = MenuItem('JumpBy', self.on_jumpby_callback)
        ScaleTo = MenuItem('ScaleTo', self.on_scaleto_callback)
        ScaleBy = MenuItem('ScaleBy', self.on_scaleby_callback)
        RotateTo = MenuItem('RotateTo', self.on_rotateto_callback)
        RotateBy = MenuItem('RotateBy', self.on_rotateby_callback)
        FadeIn = MenuItem('FadeIn', self.on_fadein_callback)
        FadeOut = MenuItem('FadeOut', self.on_fadeout_callback)
        FadeTo = MenuItem('FadeTo', self.on_fadeto_callback)

        x = 120
        y = 600
        step =50

        # 创建菜单
        self.create_menu([MoveTo, MoveBy, JumpTo, JumpBy,ScaleTo,ScaleBy,
                          RotateTo,RotateBy,FadeIn,FadeOut,FadeTo],
                         layout_strategy=fixedPositionMenuLayout(
                             [(x, y),
                              (x, y - step),
                              (x, y - step * 2),
                              (x, y - step * 3),
                              (x, y - step * 4),
                              (x, y - step * 5),
                              (x, y - step * 6),
                              (x, y - step * 7),
                              (x, y - step * 8),
                              (x, y - step * 9),
                              (x, y - step * 10)
                              ]
                         ))

    def on_moveto_callback(self):
        print("call on_moveto_callback")
        hero.do(MoveTo((100, 100), duration=2))

    def on_moveby_callback(self):
        print("call on_moveby_callback")
        hero.do(MoveBy((500, 320), duration=2))

    def on_jumpby_callback(self):
        print("call on_jumpby_callback")
        hero.do(JumpBy((200, 200), height=30, jumps=5, duration=2))

    def on_jumpto_callback(self):
        print("call on_jumpto_callback")
        hero.do(JumpTo((850, 450), height=30, jumps=5, duration=2))

    def on_scaleby_callback(self):
        print("call on_scaleby_callback")
        hero.do(ScaleBy(0.2,1))

    def on_scaleto_callback(self):
        print("call on_scaleto_callback")
        hero.do(ScaleTo(0.02, 1))

    def on_rotateto_callback(self):
        print("call on_rotateto_callback")
        hero.do(RotateTo(30, 3))

    def on_rotateby_callback(self):
        print("call on_rotateby_callback")
        hero.do(RotateBy(30, 3))

    def on_fadein_callback(self):
        print("call on_fadein_callback")
        hero.do(FadeIn(2))

    def on_fadeout_callback(self):
        print("call on_fadeout_callback")
        hero.do(FadeOut(2))

    def on_fadeto_callback(self):
        print("call on_fadeto_callback")
        hero.do(FadeTo(100, 2))

if __name__ == "__main__":
    # 初始化导演
    director.init(width=1136, height=640, caption="间隔动作")

    # 创建一个场景，并将HelloWorld层实例添加到场景中
    main_scene = Scene(BackGroud())
    main_scene.add(MainMenu())

    # 开始启动main_scene场景
    director.run(main_scene)
