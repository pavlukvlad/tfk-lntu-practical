
my_dict = {
    1: "один",
    2: "два",
    3: "двадцять два",
    4: "чотири",
    5: "нуль",
    6: "вісім",
    7: "чотири",
    8: "десять",
    9: "двадцять",
    10: "мільйон"
}


my_dict[2] = "два реборн"
my_dict[7] = "чотири реборн"


del my_dict[3]


if 4 in my_dict:
    del my_dict[4]


print(my_dict)