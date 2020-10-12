this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))

# at first, this and that are two list with equal values, but not the same list
# after, that becomes an alias for this, and the two names refer to the same list
