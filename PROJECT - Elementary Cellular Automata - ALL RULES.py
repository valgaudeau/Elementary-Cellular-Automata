rule = int(input("Hey, enter the rule you would like to see: "))

bd = [0, 0, 0, 0, 0, 0, 0, 0]

# In order to be able to use all the rules, we need to convert the numbers in binary code.
# In order to do this, we have to take the modulus of the inputted decimal divided by 2, and then keep decreasing by dividing that result by 2.
# The final combination of eight 0's and 1's also needs to be "reversed" in order to get the binary number conversion, which is why we're moving with -1.
for i in range(7, -1, -1):
    bd[i] = rule % 2
    rule = rule // 2


megalist = []

# We append all the possible combinations of neighborhoods in a megalist (instead of having individual separate lists, so we have less code).
megalist.append([1, 1, 1])
megalist.append([1, 1, 0])
megalist.append([1, 0, 1])
megalist.append([1, 0, 0])
megalist.append([0, 1, 1])
megalist.append([0, 1, 0])
megalist.append([0, 0, 1])
megalist.append([0, 0, 0])


# import random
import time

current_generation = []

for i in range(70):
    # First we assign the number of cells with the value 0 which we want to the left of our 1.
    current_generation.append(0)
current_generation.append(1)
# Now we assign the number of cells with the value 0 to the right of our 1.
for i in range(50):
    current_generation.append(0)

# Control of the number of iterations.
for gen_count in range(50):

    for x in range(len(current_generation)):
        if current_generation[x] == 1:
            print(u"\u2588", end='')
            print(u"\u2588", end='')
        else:
            print("  ", end='')
    print("")

    time.sleep(0.2)

    next_generation = []

    next_generation.append(current_generation[0])

    for i in range(len(current_generation) - 2):
        # Here we create our neighborhood of 3 cells which we want to look at, and we place it in the variable "current list".
        # The reason we include -2 here is that we don't want to look at the first and last values.
        current_list = []
        current_list.append(current_generation[i])
        current_list.append(current_generation[i + 1])
        current_list.append(current_generation[i + 2])

        # Now we compare our neighborhood to the original lists we had, and we use that to determine the values to append to our new list.
        # The way that we've setup our program is to have the 8 possible configurations at the same index as what the rules give for that solution.
        # And the representation of what the rule gives for the configuration is the binary translation of the decimal rule number.
        for e in range(8):
            if current_list == megalist[e]:
                next_generation.append(bd[e])

    # Now we just append the value at the last index:
    next_generation.append(current_generation[len(current_generation) - 1])

    current_generation = next_generation
