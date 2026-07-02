import random

if __name__ == "__main__":
    heads = int(0)

    print("Tossing a coin...")

    for i in range(3):
        print(f"Round {i + 1} : ", end="")

        if random.randint(0,1) == 0:
            print("Heads")
            heads += 1
        else:
            print("Tails")

    print(f"Heads: {heads}, Tails: {int(3) - heads}")