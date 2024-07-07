from src.generate import QHA


def question(n):
    print(f"{n}. " + QHA[f"q{n}"])


def hint(n):
    print(QHA[f"h{n}"])


def answer(n):
    print(QHA[f"a{n}"])
