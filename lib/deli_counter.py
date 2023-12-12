katz_deli = []


def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        print(
            "The line is currently: "
            + " ".join(f"{index + 1}. {name}" for index, name in enumerate(katz_deli))
        )


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")


def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        serving_person = katz_deli.pop(0)
        print(f"Currently serving {serving_person}.")
