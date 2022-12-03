
def get_the_nmost_amount_of_calories(n:int, total_calories:list):
    n_max_calories = []
    for i in range(n):
        max_calories = max(total_calories)
        n_max_calories.append(max_calories)
        total_calories.remove(max_calories)
    return n_max_calories
        

calories_file = open("../inputs/calories.txt", 'r')
calories = calories_file.readlines()
total_calories = []
current_elf_calories = []
NUMBER_OF_TOP_ELVES = 3

for calorie in calories:
    if calorie == '\n':
        total_calories.append(sum(current_elf_calories))
        current_elf_calories = []
        continue
    cal = int(calorie.rstrip("\n"))
    current_elf_calories.append(cal)

max_calories = max(total_calories)
print(f"The elf that is eating the most has eaten a grand total of {max_calories} calories!")

n_max_calories = sum(get_the_nmost_amount_of_calories(NUMBER_OF_TOP_ELVES, total_calories.copy()))
print(f"The {NUMBER_OF_TOP_ELVES} elves that have eaten the most have eaten a grand total of {n_max_calories} calories!")