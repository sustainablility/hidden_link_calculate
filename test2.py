
def recu(integer):
    if integer > 0:
        return integer + recu(integer - 1)
    else:
        return integer

print(recu(3))
# expect : 6