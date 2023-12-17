def main():
    vegetables = "Is anyone in your party a vegetarian (Yes/No)"
    vegetarian = input(vegetables)
    print(vegetarian)
    vegans = "Is anyone in your party a vegan (Yes/No)"
    vegan = input(vegans)
    print(vegan)
    gluten = "Is anyone in your party gluten-free (Yes/No)"
    gluten_free = input(gluten)
    print(gluten_free)
    print("Here are your restaurant choices:")

    diet_choice(gluten_free, vegan, vegetarian)


def diet_choice(gluten_free, vegan, vegetarian):
    if vegetarian == "Yes" and vegan == "Yes" and gluten_free == "Yes":
        print("Corner cafe'")
        print("The Chef's Kitchen")
    elif vegetarian == "Yes" and vegan == "Yes" and gluten_free == "No":
        print("Corner cafe'")
        print("The Chef's Kitchen")
    elif vegetarian == "Yes" and vegan == "No" and gluten_free == "Yes":
        print("Main Street Pizza")
        print("Corner Cafe'")
        print("The Chef's Kitchen")
    elif vegetarian == "Yes" and vegan == "No" and gluten_free == "No":
        print("Main Street Pizza")
        print("Corner Cafe'")
        print("Luigi's Fine Italian Restaurant")
        print("The Chef's Kitchen")
    elif vegetarian == "No" and vegan == "No" and gluten_free == "No":
        print("Joes' Gourmet Burgers")
        print("Main Street Pizza")
        print("Corner Cafe'")
        print("Luigi's Fine Italian Restaurant")
        print("The Chef's Kitchen")
    elif vegetarian == "No" and vegan == "No" and gluten_free == "Yes":
        print("Main Street Pizza")
        print("Corner Cafe'")
        print("The Chef's Kitchen")
    elif vegetarian == "No" and vegan == "Yes" and gluten_free == "Yes":
        print("Corner cafe'")
        print("The Chef's Kitchen")
    elif vegetarian == "No" and vegan == "Yes" and gluten_free == "No":
        print("Corner cafe'")
        print("The Chef's Kitchen")
    else:
        print("Invalid answer")


main()
