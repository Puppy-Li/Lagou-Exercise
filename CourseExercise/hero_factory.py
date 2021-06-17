from CourseExercise.hero import Timo, Jinx

class HeroFactory:
    def create_hero(self, hero):
        if hero == "timo":
            return Timo()
        elif hero == "jinx":
            return Jinx()
        else:
            raise Exception("此英雄不在英雄工厂当中")


hero_factory = HeroFactory()
jinx = hero_factory.create_hero("jinx")
timo = hero_factory.create_hero("timo")
timo.fight(jinx.hero_hp, jinx.hero_power, jinx.hero_name)