import numpy as np


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| F-Stop Ratios |")
    print("-----------------\n")

    from_ratios()

    # from_light()

    # from_stops()


def ratios_to_light(ratios):

    '''
    Calculate the fraction of light the 
    ratios transfer relative to f1.0
    1.0 / 1.0² = 1
    1.0 / 1.4² = 0.51
    etc.
    '''

    return 1 / ratios**2


def light_to_stops(light):

    '''
    Calculate the reduction in stops
    corresponding to the light fraction
    -(np.log2(1 / 1.0)) = 0
    -(np.log2(1 / 0.51)) = -0.97
    etc.
    '''

    return -(np.log2(1 / light))


def light_to_ratios(light):

    '''
    Calculate the  stop ratios
    corresponding to the light fractions
    1 / 1^0.5 = 1
    1 / 0.5^0.5 = 1.41
    etc.
    '''

    return 1/light**0.5


def stops_to_light(stops):

    '''
    Calculate light fractions
    from f stop ratios
    1/2^-0 = 1
    1/2^--1 = 0.5
    '''

    return 1/2**-stops


def from_ratios():

    '''
    Create an array of f stop ratios
    f1.0 to f5.6
    and calculate corresponding light
    fractions and reductions in stops
    '''

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

    '''
    Create an array of light fractions
    from 1.0 to 0.001953
    each half the previous.
    Then calculate the corresponding
    stop reductions and ratios.
    '''

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

    '''
    Create an array of stop reductions
    from 0 to -9
    and calculate corresponding
    light fractions and f ratios.
    '''

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
