# -*- coding:utf-8 -*-
# Author:Alfred

from cocos.layer import *
from cocos.menu import *
from cocos.scene import *
from cocos.director import *
from cocos.sprite import *
from cocos.actions import *
from cocos.particle_systems import *


# 创建一个全局变量
game_layer = None

# 创建一个自定义的背景层
class BackGroud(Layer):

    def __init__(self):
        super(BackGroud, self).__init__()

        # 创建初始的粒子系统
        sp = Spiral()
        sp.position = 560,320

        # 把精灵添加进层,并设置一个名字
        self.add(sp, name='particle')

# 自定义MainMenu层类
class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__()

        # 创建菜单字体，颜色,及选中字体时的颜色
        self.font_item['font_size'] = 20
        self.font_item['color'] = (255, 255, 255, 255)
        self.font_item_selected['font_size'] = 26
        self.font_item_selected['color'] = (123, 123, 123, 255)

        # 设置图片项
        fireworks = MenuItem('Fireworks', self.on_fireworks_callback)
        spiral = MenuItem('Spiral', self.on_spiral_callback)
        meteor = MenuItem('Meteor', self.on_meteor_callback)
        sun = MenuItem('Sun', self.on_sun_callback)
        fire = MenuItem('Fire', self.on_fire_callback)
        galaxy = MenuItem('Galaxy', self.on_galaxy_callback)
        flower = MenuItem('Flower', self.on_flower_callback)
        explosion = MenuItem('Explosion', self.on_explosion_callback)
        smoke = MenuItem('Smoke', self.on_smoke_callback)

        x = 120
        y = 600
        step =50

        # 创建菜单
        self.create_menu([fireworks, spiral, meteor, sun, fire, galaxy,
                          flower, explosion, smoke],
                         layout_strategy=fixedPositionMenuLayout(
                             [(x, y),
                              (x, y - step),
                              (x, y - step * 2),
                              (x, y - step * 3),
                              (x, y - step * 4),
                              (x, y - step * 5),
                              (x, y - step * 6),
                              (x, y - step * 7),
                              (x, y - step * 8)
                              ]
                         ))

    def on_fireworks_callback(self):
        print("call on_fireworks_callback")
        game_layer.remove('particle')
        sp = Fireworks()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_spiral_callback(self):
        print("call on_spiral_callback")
        game_layer.remove('particle')
        sp = Spiral()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_meteor_callback(self):
        print("call on_meteor_callback")
        game_layer.remove('particle')
        sp = Meteor()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_sun_callback(self):
        print("call on_sun_callback")
        game_layer.remove('particle')
        sp = Sun()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_fire_callback(self):
        print("call on_fire_callback")
        game_layer.remove('particle')
        sp = Fire()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_galaxy_callback(self):
        print("call on_galaxy_callback")
        game_layer.remove('particle')
        sp = Galaxy()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_flower_callback(self):
        print("call on_flower_callback")
        game_layer.remove('particle')
        sp = Flower()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_explosion_callback(self):
        print("call on_explosion_callback")
        game_layer.remove('particle')
        sp = Explosion()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_smoke_callback(self):
        print("call on_smoke_callback")
        game_layer.remove('particle')
        sp = Smoke()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

if __name__ == "__main__":
    # 初始化导演
    director.init(width=1136, height=640, caption="粒子系统")

    game_layer = BackGroud()
    # 创建一个场景，并将HelloWorld层实例添加到场景中
    main_scene = Scene(game_layer)
    main_scene.add(MainMenu())

    # 开始启动main_scene场景
    director.run(main_scene)
