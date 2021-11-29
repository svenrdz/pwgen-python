import random
import typing as t
from string import ascii_letters, digits  # , punctuation

from .utils import assert_natural


class Pwgen:
    def __init__(
        self,
        pw_length: int = 8,
        num_pw: int = 1,
        seed: t.Optional[str] = None,
    ):
        assert_natural("pw_length", pw_length)
        assert_natural("num_pw", num_pw)
        self.pw_length = pw_length
        self.num_pw = num_pw
        self.charset = ascii_letters + digits
        self.random = random.Random(seed)

    def randchar(self):
        return self.random.choice(self.charset)

    def generate_one(self):
        pw = ""
        while len(pw) < self.pw_length:
            nextchar = self.randchar()
            pw += nextchar
        return pw

    def generate(self):
        result = []
        for _ in range(self.num_pw):
            result.append(self.generate_one())
        return result
