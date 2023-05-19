class Recipe:
    def __init__(self, *args):
        self.__args = []
        #print(type(self.__args))
        for a in args:
            self.__args.append(a)
        #self.__args = args

    def add_ingredient(self, ing):  # добавление нового ингредиента ing (объект класса Ingredient) в рецепт (в конец);
        self.__args.append(ing)

    def remove_ingredient(self, ing):  # удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта;
        self.__args.remove(ing)

    def get_ingredients(self):
        return tuple(self.__args)

    def __len__(self):
        return len(self.__args)


class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe)  # n = 3

print(n)