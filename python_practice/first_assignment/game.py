'''
一个多回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
'''
#定义一个函数game
def game ( ):
    #引用random模块
    import  random
    #对my_hp进行赋值、对your_hp进行赋值
    my_hp=1000
    your_hp=1000
    #调用random模块中的randint函数对my_power和your_power进行赋值
    #my_power和your_power是在（1-100）中随机生成的一个数，不包含1和100
    my_power=random.randint(1,100)
    your_power=random.randint(1,100)
    #进入while循环体 为真进行循环
    while True :
        #受到攻击后，我的血量
        my_hp=my_hp-your_power
        print("我的当前血量：",my_hp)
        #收到攻击后，你的血量
        your_hp=your_hp-my_power
        print("你的当前血量：",your_hp)
        #判断语句 如果my_hp<0
        if my_hp<=0:
        #为真，打印语句你赢了，跳出循环体，结束循环；为假，去执行elif条件判断
         print("你赢了")
         break
        #判断语句 如果your_hp<0
        elif your_hp<=0:
        #为真，打印语句我赢了，跳出循环体，结束循环；为假继续进行在循环体中循环
            print("我赢了")
            break
    #打印出我此次随机生成的攻击力数值，和结束时我的血量；
    #打印出你此次随机生成的攻击力数值，和结束时你的血量；
    print("我的攻击力:%d 我的血量:%d"%(my_power, my_hp))
    print("你的攻击力:%d 你的血量:%d"%(your_power, your_hp))
#调用game函数
game()