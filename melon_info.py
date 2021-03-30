"""Print out all the melons in our inventory."""
# Create a dictionary with the keys being the melon type 
# and the values being everything else

from melons import melons


# def print_melon(melons):
    
#     for name, attribute in melons:
#         print(name, attribue)

# def print_melon()


def print_all_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon_name, attributes in melons.items():
        print(melon_name.upper())

        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

        print('===================================')


print_all_melons(melons)