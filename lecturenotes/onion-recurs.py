def peel_onion(layers_left):
    if layers_left == 0:
        print("The onion is peeled!")
        return 
    else:
        print(f"Peeling layer {layers_left}")
        layers_left -= 1
        peel_onion(layers_left )
        print(f"Peeling layer {layers_left}")

peel_onion(5)
