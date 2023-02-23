import numpy as np


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| F-Stop Ratios |")
    print("-----------------\n")

    # from_ratios()

    # from_light()

    # from_stops()


def ratios_to_light(ratios):

    return 1 / ratios**2


def light_to_stops(light):

    return -(np.log2(1 / light))


def light_to_ratios(light):

    return 1/light**0.5


def stops_to_light(stops):

    return 1/2**-stops


def from_ratios():

    ratios = np.arange(1, 5.7, 0.1)

    light = ratios_to_light(ratios)

    stops = light_to_stops(light)

    print("------------------------")
    print("|  f  | light |  stops |")
    print("------------------------")

    for i in range(0, len(ratios)):

        print(f"| {ratios[i]:.1f} | {light[i]:.3f} |  {stops[i]:.2f} |")

    print("------------------------")


def from_light():

    light = np.fromfunction(lambda n: 1/(2**n), (10,))

    stops = light_to_stops(light)

    ratios = light_to_ratios(light)

    print("----------------------------")
    print("|  light   | stops |   f   |")
    print("----------------------------")

    for i in range(0, len(light)):

        print(f"| {light[i]:.6f} | {stops[i]:.1f}  | {ratios[i]:>5.2f} |")

    print("----------------------------")


def from_stops():

    stops = np.arange(-0, -10, -1)

    light = stops_to_light(stops)

    ratios = light_to_ratios(light)

    print("--------------------------")
    print("| stops | light |    f   |")
    print("--------------------------")

    for i in range(0, len(stops)):

        print(f"|  {stops[i]:>4.1f} | {light[i]:.3f} |   {ratios[i]:>4.1f} |")

    print("--------------------------")


if __name__ == "__main__":

    main()
