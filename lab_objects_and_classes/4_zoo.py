mammals = []
birds = []
fishes = []

class Zoo:
    __animals = 0
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name
        self.birds = []
        self.fishes = []
        self.mammals = []


    def add_animal(self,species, name):
        if species == "mammals":
            self.mammals.append(name)
        elif species == "birds":
            mammals.append(name)
        elif species == "fishes":
            mammals.append(name)
        Zoo.__animals += 1

    def get_info(self, specie):
        result = ""
        if specie == "mammal":
            result += f"Mammals in {self.zoo_name}:{", ".join(self.mammals)}\n"
        elif specie == "fish":
            result += f"Fishes in {self.zoo_name}:{", ".join(self.fishes)}\n"
        elif specie == "bird":
            result += f"Birds in {self.zoo_name}:{", ".join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
iter = int(input())
for i in range(iter):
    animal = input().split(" ")
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species,name)
info = input()
print(zoo.get_info(info))