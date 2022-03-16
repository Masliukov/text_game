def read_q(i):
    with open("questions.txt", "r") as f:
        text = f.readlines()
        return text[i-1]

