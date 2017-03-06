# def draw_stars(array):
#     for x in array:
#         print "*" * x

# array = [2, 4, 6, 8, 10]
# draw_stars(array)


def draw_stars_advanced(array):
    for x in array:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            print x[0].lower() * len(x)

array = [2, 4, "Waldo", "king kong", 8, 10]
draw_stars_advanced(array)


