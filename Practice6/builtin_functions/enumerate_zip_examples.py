"""Pair values using enumerate and zip."""


def main():
    names = ["Aida", "Daniyar", "Mira"]
    scores = [91, 84, 97]
    print("Enumerate names:")
    for index, name in enumerate(names, start=1):
        print(index, name)

    print("Zipped name/score pairs:")
    for name, score in zip(names, scores):
        print(f"{name}: {score}")


if __name__ == "__main__":
    main()
