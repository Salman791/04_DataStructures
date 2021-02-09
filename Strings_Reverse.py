# Create a function called 'reverse' which takes a string as a parameter
# The function reverses it and returns with the reversed string


# toBeReversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"
#
# print(reverse(toBeReversed))

def reverse(toBeReversed):
    if len(toBeReversed) == 0:
        return toBeReversed
    else:
        return reverse(toBeReversed[1:]) + toBeReversed[0]

toBeReversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"
print(reverse(toBeReversed))

