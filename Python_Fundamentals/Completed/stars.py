x = [4, 6, 1, 3, 5, 7, 25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(a):
    for count in range(0,len(a)):
        if type (a[count]) is int:
            print a[count] * "*"
        else:
            print a[count][0:1].lower() * len(a)

draw_stars(x)
draw_stars(y)
