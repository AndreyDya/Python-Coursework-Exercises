"""
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# assign copy of a list
areas_copy1 = areas[:]
# assign a list
areas_copy2 = areas
areas_copy1[0] = 11.75
print(areas)
areas_copy2[0] = 11.75
print(areas)
# single responsibility principle
"""


def volume_calc(length, width, height):
    volume = length * width * height
    return volume


print(volume_calc(20, 10, 5))
