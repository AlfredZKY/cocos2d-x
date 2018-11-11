# -*- coding:utf-8 -*-
# Author:Alfred
from cocos.menu import *
from cocos.scene import *
from cocos.layer import *
from cocos.director import *
from cocos.sprite import *
from cocos.scenes.transitions import *
from cocos.audio.pygame import music
from cocos.audio.effect import Effect

import Setting

# 创建一个自定义的背景层
class BackGroud(Layer):

    def __init__(self):
        super(BackGroud, self).__init__()

        # 获取窗口的大小
        self.width, self.height = director.get_window_size()
        # 创建背景精灵
        backgroud = Sprite('images/game-bg.png')
        backgroud.position = self.width // 2, self.height //2

        # 把精灵添加进层
        self.add(backgroud)



# 自定义MainMenu层类
class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__()

        # 创建菜单字体，颜色,及选中字体时的颜色
        self.font_item['font_size'] = 160
        self.font_item['color'] = (255, 255, 255, 255)
        self.font_item_selected['font_size'] = 160
        self.font_item_selected['color'] = (230, 230, 230, 255)

        # 设置图片菜单项
        start_item = ImageMenuItem('images/start-up.png', self.on_start_item_callback)
        set_item = ImageMenuItem('images/setting-up.png', self.on_set_item_callback)
        help_item = ImageMenuItem('images/help-up.png', self.on_help_item_callback)

        # 创建菜单
        self.create_menu([start_item, set_item, help_item],
                         layout_strategy=fixedPositionMenuLayout(
                             [(800, 480), (480, 370), (900, 250)]
                         ))

    def on_start_item_callback(self):
        print("call on_start_item_callback")
        effect = Effect('sound/Blip.wav')
        effect.play()

    def on_set_item_callback(self):
        print("call on_set_item_callback")
        effect = Effect('sound/Blip.wav')
        effect.play()
        # new_scene = Setting.create_scene()
        # director.push(new_scene)
        new_scene = Setting.create_scene()
        # dst = RotoZoomTransition(new_scene, 1.2)
        # dst = JumpZoomTransition(new_scene, 1.2)
        dst = SlideInLTransition(new_scene, 1.2)
        director.push(dst)



    def on_help_item_callback(self):
        print("call on_help_item_callback")

if __name__ == "__main__":
    # 初始化导演
    director.init(width=1136, height=640, caption="场景切换", audio_backend='sdl')

    # 创建一个场景，并将HelloWorld层实例添加到场景中
    main_scene = Scene(BackGroud())
    main_scene.add(MainMenu())

    # 播放背景音乐
    music.load('sound/Synth.ogg'.encode())
    music.play(loops=-1)
    music.set_volume(1.0)

    # 开始启动main_scene场景
    director.run(main_scene)
