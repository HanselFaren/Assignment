favourite_cars ={
    "JJ": ("Golf", "Camry", "LFA"),
    "Nicklas": ("Innova", "Panther", "Fortuner"),
    "Hansel": ("Skyline", "Supra", "RX7"),
    "Strad": ("Aventador", "Murcielago", "Gallardo"),
    "DDE": ("Veyron", "Chiron", "Centodieci")
}

for key, value in favourite_cars.items():
    print(key, "likes these cars:")
    im_a_string = ""

    for i in value[0]:
        im_a_string += i + ""

    print("-", im_a_string.rstrip())
    print("-", value[1])
    print("-", value[2])