import random


class Pwgen:
    LINE_MAXLEN = 80
    NUM_LINES = 20

    def __init__(self, seed=None, pw_length=8, num_pw=None):
        self.random = random.Random(seed)
        self.pw_length = pw_length
        if num_pw is None:
            nb_per_line = Pwgen.LINE_MAXLEN // (self.pw_length + 1)
            self.num_pw = Pwgen.NUM_LINES * nb_per_line
        else:
            self.num_pw = num_pw

    def generate_one(self):
        return "a" * self.pw_length

    def generate(self):
        result = []
        for _ in range(self.num_pw):
            result.append(self.generate_one())
        return result

    def format(self, passwords):
        passwords = self.generate()
        if Pwgen.LINE_MAXLEN > self.pw_length * 2 + 1:
            lines = [""]
            for pw in passwords:
                line = lines[-1]
                if len(line) > 0:
                    line += " "
                line += pw
                if len(line) >= Pwgen.LINE_MAXLEN:
                    lines.append(pw)
                else:
                    lines[-1] = line
        else:
            lines = passwords
        return "\n".join(lines)

    def run(self):
        return self.format(self.generate())
