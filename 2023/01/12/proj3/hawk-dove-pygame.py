import random
import pygame

random.seed()

#Constants: setting these values controls the parameters of your experiment.
injurycost = 10 #Cost of losing a fight  
displaycost = 1 #Cost of displaying   
foodbenefit = 8 #Value of the food being fought over   
init_hawk = 0
init_dove = 0
init_defensive = 0
init_evolving = 100

def plot(xvals, yvals, canvas, surface):
    # This is a function for creating a simple scatter plot.  You will use it,
    # but you can ignore the internal workings.
    w,h = canvas.get_width(), canvas.get_height()
    canvas.fill('black')
    #plot the points
    for i in range(len(xvals)):
        x, y = xvals[i], yvals[i]
        xpixel = int(50 + ((w-100)//2)*(x-1))
        ypixel = int(h-50 - (h-100)*y)
        pygame.draw.circle(canvas, 'red', (xpixel,ypixel), 2)
    surface.blit(canvas, (0,0))
    pygame.display.flip()

########
# Your code here
########

class World:
    def __init__(self, canvas, surface):
        self.population = []
        self.speciesHistogram = {}
        self.canvas = canvas
        self.surface = surface

    def add_being(self, new_being):
        self.population.append(new_being)
        # print("adding a ", new_being.species , " population is now ", len(self.population))
        self.speciesHistogram[new_being.species] = 0

    # update all of the world's beings
    def update(self):
        for being in self.population:
            being.update()

    # process the availablility of food
    def free_food(self, count):
        discoverer = random.choice(self.population)
        discoverer.eat()

    def conflict(self, numEncounters):
        for i in range(numEncounters):
            conflictees = random.choices(self.population, k=2)
            conflictees[0].encounter(conflictees[1])

    def status(self):
        hawkCount = 0
        doveCount = 0
        for species in self.speciesHistogram:
            self.speciesHistogram[species] = 0

        for bird in self.population:
            self.speciesHistogram[bird.species] += 1

        print("In the world there are:")

        for species in self.speciesHistogram:
            print(self.speciesHistogram[species], " ", species, "s ")

    def evolvingPlot(self):
        weights = []
        aggressions = []
        for bird in self.population:
            weights.append(bird.weight)
            aggressions.append(bird.aggression)

        plot(weights, aggressions, self.canvas, self.surface)

class Bird:
    species = "undefined"

    def __init__(self, world):
        self.world = world
        self.health = 100
        self.world.add_being(self)

    # eat (and heal)
    def eat(self):
        self.health += foodbenefit

    # sustain an injury
    def injured(self):
        self.health -= injurycost

    # scare off another bird, costs health
    def display(self):
        self.health -= displaycost

    # this bird has died, remove self from world
    def die(self):
        self.world.population.remove(self)

    def update(self):
        self.health -= 1
        if self.health <= 0:
            self.die()


class Dove(Bird):
    species = "Dove"

    def update(self):
        super().update()
        if self.health > 200:
            self.health -= 100
            hatchling = Dove(self.world)

    def defend_choice(self):
        return False

    # model this Dove encountering another bird with food
    def encounter(self, otherBird):
        print(self.species, "is encountering a", otherBird.species, ": ", end='')
        if otherBird.defend_choice():
            otherBird.eat()
            print("I lose")
        else:
            self.display()
            otherBird.display()
            if random.random() > 0.5:
                self.eat()
                print("I win display", self.species)
            else:
                otherBird.eat()
                print("I lose display", self.species)


class Hawk(Bird):
    species = "Hawk"

    def update(self):
        super().update()
        if self.health > 200:
            self.health -= 100
            hatchling = Hawk(self.world) # this adds to the world

    def defend_choice(self):
        return True

    def encounter(self, otherBird):
        if otherBird.defend_choice():
            if random.random() > 0.5:
                self.eat()
                otherBird.injured()
            else:
                otherBird.eat()
                self.injured()
        else:
            self.eat()

class Defensive(Dove):
    species = "Stellar's Jay"

    def update(self):
        Bird.update(self)
        if self.health > 200:
            self.health -= 100
            print("Jay reproducing!")
            hatchling = Defensive(self.world) # this adds to the world

    def defend_choice(self):
        return True

# returns a new x that is between min and max
def forceRange(x, min, max):
    if x < min:
        x = min
    elif x > max:
        x = max
    return x

class Evolving(Bird):
    species = "Evolving"

    def __init__(self, world, weight = None, aggression = None):
        super().__init__(world)
        # weight is not None if we have a parent
        if weight is not None:
            self.weight = forceRange(weight + random.uniform(-0.1, 0.1), 1, 3)
        else:
            # no parent, so randomize
            self.weight = random.uniform(1,3)

        if aggression is not None:
        # weight is not None if we have a parent
            self.aggression = forceRange(aggression + random.uniform(-0.05, 0.05), 0, 1)
        else:
            # no parent, so randomize
            self.aggression = random.uniform(0,1)

    def update(self):
        self.health -= 0.4 * 0.6*self.weight
        if self.health <= 0:
            self.die()
        elif self.health > 200:
            self.health -= 100
            hatchling = Evolving(self.world, self.weight, self.aggression)

    def defend_choice(self):
        d100 = random.uniform(0,1)
        # the bigger my aggression, the more likely I'm going to defend my choice
        return d100 < self.aggression

    def encounter(self, other):
        if other.defend_choice():
            if self.defend_choice():
                # we're both aggressive: we fight
                pWin = self.weight / (self.weight + other.weight)
                d100 = random.uniform(0,1)
                if d100 < pWin:      # my weight overpowered other
                    self.eat()
                    other.injured()
                else:                # my weight underwhelmed other
                    other.eat()
                    self.injured()
            else:
                # other is aggressive, I'm chill: I yield
                other.eat()
        elif self.defend_choice():
            # other's chill, I'm hangry: just eat
            self.eat()
        else:
            # neither aggressive: act like doves
            self.display()
            other.display()
            random.choice([self,other]).eat()


########
# The code below actually runs the simulation.  You shouldn't have to do anything to it.
########
WINDOW_WIDTH=700
WINDOW_HEIGHT=400
pygame.init()
plot_window  = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
plot_surface = pygame.display.get_surface()
plot_canvas  = pygame.Surface([WINDOW_WIDTH,WINDOW_HEIGHT])

w = World(plot_surface, plot_canvas)
for i in range(init_dove):
    Dove(w)
for i in range(init_hawk):
    Hawk(w)
for i in range(init_defensive):
    Defensive(w)
for i in range(init_evolving):
    Evolving(w)

w.status()

for t in range(10000):
    w.free_food(10) 
    w.conflict(50)
    w.update()
    w.evolvingPlot()
    input()
w.status()


