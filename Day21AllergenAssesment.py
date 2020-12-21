# Could easily be refactored into dict
class Food:
    def __init__(self, ingredients, allergens):
        self.ingredients = ingredients
        self.allergens = allergens


    def __repr__(self):
        return 'Food(' + str(self.ingredients) + ', ' + str(self.allergens) + ')'

    # Unused
    def __and__(self, other):
        return self.ingredients & other.ingredients, self.allergens & other.allergens


foods = []
ingredient_set = set()
allergen_set = set()
allergen_match_dict = dict()

# Parsing Input into set of ingredients, allergens, and list of food.
with open("Menu") as menu_txt:
    for food in menu_txt.read().splitlines():
        ingredients, allergens = food.split(' (contains ')

        allergens = set(allergens.strip(')').split(', '))
        allergen_set |= allergens

        ingredients = set(ingredients.split())
        ingredient_set |= ingredients

        foods.append(Food(ingredients, allergens))

# Find allergens by intersecting all ingredient sets with an arbitrary allergen.
# If only one remains, remove from main ingredient set.
while allergen_set:

    # Keeps track of allergens to remove after running through for loop
    to_remove = set()

    for allergen in allergen_set:
        f = set(ingredient_set)
        for food in [food for food in foods if allergen in food.allergens]:
            f &= food.ingredients

        if len(f) == 1:
            ingredient_set -= f
            to_remove.add(allergen)
            allergen_match_dict[allergen] = next(iter(f))

    allergen_set -= to_remove

# Since we removed ingredients with an allergen, all that remains are ingredients without allergens
cnt = 0
for food in foods:
    cnt += len(food.ingredients & ingredient_set)

print(cnt)  # Part 1

s = ''
for k in sorted(allergen_match_dict.keys()):
    s += allergen_match_dict[k] + ','

print(s.strip(','))  # Part 2
