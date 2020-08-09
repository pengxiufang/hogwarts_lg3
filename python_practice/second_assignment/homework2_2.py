from python_practice.second_assignment.homework2_1 import TongLao


class Xuzhu(TongLao):
    def __init__(self, hp, power):
        super().__init__(hp, power)

    def read(self, name):
        print("罪过罪过")


xz = Xuzhu(100, 9)
xz.fight_zms("李四", 200, 20)
xz.read("虚竹")