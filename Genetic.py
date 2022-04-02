import random
import math

# menggunakan tipe integer
def generate_population(size, batasX, batasY):
    batasBawahX, batasAtasX = batasX
    batasBawahY, batasAtasY = batasY

    population = []
    for i in range(size):
        individu = {
            #dekode kromosomnya
            "x": random.randint(batasBawahX, batasAtasX),
            "y": random.randint(batasBawahY, batasAtasY),
        }
        population.append(individu)

    return population

def calculate_fitness(individu):
    #rumus fitness
    x = individu["x"]
    y = individu["y"]
    return ((math.cos(x) + math.sin(y))**2)/((x**2 + y**2)) 

#buat elitism
def sort_by_fitness(population):
    return sorted(population, key=calculate_fitness, reverse=True) # mengurutkan berdasarkan nilai minimal

def roulette_wheel(sorted_population, fitness_sum):
    offset = 0
    normalized_fitness_sum = fitness_sum

    lowest_fitness = calculate_fitness(sorted_population[0])
    if lowest_fitness < 0:
        offset = -lowest_fitness
        normalized_fitness_sum += offset * len(sorted_population)
        
    accumulation = 0
    draw = random.randint(0, 1)
    for individu in sorted_population:
        fitness = calculate_fitness(individu) + offset
        probability = fitness / fitness_sum
        accumulation += probability

        if draw <= accumulation:
            return individu
        
# pakai satu titik      
def crossover(individu_a, individu_b):
    xa = individu_a["x"]
    ya = individu_a["y"]
    xb = individu_b["x"]
    yb = individu_b["y"]

    return {"x": xb, "y": ya}

def mutation(individu):
    
    next_x = random.randint(batasBawahX, batasAtasX)
    next_y = random.randint(batasBawahY, batasAtasY)

    return {"x": next_x, "y": next_y}

def generation_new(population_before):
    generation_after = []
    sorted_by_fitness_population = sort_by_fitness(population_before)
    #elitism dipotong disini
    population_size = len(population_before)
    fitness_sum = sum(calculate_fitness(individu) for individu in population)

    i = 0
    while i <(population_size):
        ortu_1 = roulette_wheel(sorted_by_fitness_population, fitness_sum)
        ortu_2 = roulette_wheel(sorted_by_fitness_population, fitness_sum)

        if random.randint(-5, 5) < 10 :   
            individu = crossover(ortu_1, ortu_2)
            individu = mutation(individu)
            generation_after.append(individu)
        else :
            generation_after.append(ortu_1)
        i+=1

    return generation_after

batasBawahX, batasAtasX = -5,5
batasBawahY, batasAtasY = -5,5

generations = int(input("generasi yang dibutuhkan : ", ))
population = generate_population(size=3, batasX=(-5,5), batasY=(-5,5))

i = 1
while True:
    print("generasi ke :", i)
    for individu in population:
        print(individu) 
        print("Fitnessnya :,", calculate_fitness(individu))
        fitness_sum = sum(calculate_fitness(individu) for individu in population)
        probability = calculate_fitness(individu)/fitness_sum
        print("probabilitas terpilih :", probability)
        print("-----------------------------------------------")

    if i == generations:
        break

    print("==================================================")
    print("individu terminimum di gen ini: ", sort_by_fitness(population)[-1])
    print("==================================================")
    print(" ")
    temp = sort_by_fitness(population)[-1]

    i += 1
    population = generation_new(population)
    population.append(temp)

individu_terbaik = sort_by_fitness(population)[-1]
print("==================================================")
print ("Individu terminimum yang didapatkan : ")
print(individu_terbaik)
print("Fitnessnya: ", calculate_fitness(individu_terbaik))
print("Probabilitas individu terminimum :", probability)
print("==================================================")
