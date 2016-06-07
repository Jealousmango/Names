import random
flips = 0
heads = 0
tails = 0
while flips <= 5000:
    headortail = random.randint(1,2)
    print("Attempt #{} " .format(flips))
    if headortail == 1:
        heads = heads + 1
    if headortail == 2:
        tails = tails + 1
    print("Got {} heads and {} tails so far" .format(heads, tails))
    flips = flips + 1
