from src.generate import QDHA


def question(n):
    print(f"{n}. " + QDHA[f"q{n}"])


def hint(n):
    print(QDHA[f"h{n}"])


def answer(n):
    print(QDHA[f"a{n}"])
