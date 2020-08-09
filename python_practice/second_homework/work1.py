'''
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
'''
class company:
    def __init__(self,company_name,boss,address,members):
        self.company_name=company_name
        self.boss=boss
        self.address=address
        self.members=members
    def information(self):
        print(f"公司名称{self.company_name},老板是{self.boss},地址在{self.address},成员有{self.members}")
    def Party_building(self):
        print(f"{self.members}组织一起团建")
    def paly_game(self):
        print(f"{self.members}在办公室打游戏")
    def fahognbao(self):
        print(f"{self.boss}老板发红包")
alibaba=company("阿里巴巴","马云","浙江省杭州","逍遥子")
print(f"公司名称{alibaba.company_name},老板是{alibaba.boss},地址在{alibaba.address},成员有{alibaba.members}")
alibaba.fahognbao()
tx=company("腾讯","马化腾","深圳","张三")
print(f"公司名称{tx.company_name},老板是{tx.boss},地址在{tx.address},成员有{tx.members}")
tx.paly_game()
zhp=company("杭州真会拼","王峰","浙江杭州","李四")
print(f"公司名称{zhp.company_name},老板是{zhp.boss},地址在{zhp.address},成员有{zhp.members}")
zhp.Party_building()