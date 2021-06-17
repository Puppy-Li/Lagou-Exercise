
class Hero:
    hero_hp = 1000
    hero_power = 200
    hero_name = "hero"

    def fight(self, enemy_hp, enemy_power, enemy_name):
        '''
        :param enemy_hp: 敌人的血量，是整型
        :param enemy_power: 敌人的力量，是整型
        :return:
        '''
        # 计算英雄的最终血量
        hero_final_hp = self.hero_hp - enemy_power
        # 计算敌人的最终血量
        enemy_final_hp = enemy_hp-self.hero_power
        # 判断最终谁的血量更多
        if hero_final_hp > enemy_final_hp:
            print(f"{self.hero_name}赢了")
        elif hero_final_hp < enemy_final_hp:
            print(f"敌人{enemy_name}赢了")
        else:
            print("平局")


class Timo(Hero):
    hero_hp = 1800
    hero_power = 210
    hero_name = "Timo"


class Jinx(Hero):
    hero_hp = 1200
    hero_power = 190
    hero_name = "Jinx"
