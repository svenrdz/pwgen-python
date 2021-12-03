import string
import random
import typing as t

from .utils import assert_natural, GeneratorFlags

gf = GeneratorFlags

VOWELS_STR = "aeiouy"
CONSONANTS_STR = "bcdfghjklmnpqrstvwxz"
DIGITS_STR = string.digits
SYMBOLS_STR = string.punctuation
UNAMBIGUOUS_DIGITS = "3479"
VOWEL_PHONEMES = "a,e,ea,ai,i,ia,ie,ieu,ien,y,eu,o,oi,oin,au,eau,u,ua,uan,ue,uer,ueu,ui,uin,ou,oua,an,en,em,in,im,ain,aim,ein,yn,ym,un,um,on".split(
    ","
)
CONSONANT_PHONEMES = "b,d,f,ff,ph,c,ch,qu,k,l,m,mm,n,nn,ng,gn,p,r,rr,rh,s,ss,sc,c,cr,pt,sh,t,th,tr,tt,v,w,z,j,g".split(
    ","
)

AMBIGUOUS_SET = set("B8G6I1l0OQDS5Z2")


def isambiguous(phoneme):
    return len(AMBIGUOUS_SET & set(phoneme)) > 0


class Pwgen:
    def __init__(
        self,
        pw_length: int = 8,
        num_pw: int = 1,
        flags: GeneratorFlags = gf.default(),
        seed: t.Optional[str] = None,
    ):
        assert_natural("pw_length", pw_length)
        assert_natural("num_pw", num_pw)
        self.pw_length = pw_length
        self.num_pw = num_pw
        self.flags = flags
        self.rand = random.Random(seed)
        self.required_flags = gf.Digits | gf.Symbols | gf.Uppercase
        if self.pw_length < 5:
            self.flags |= gf.Secure
        if self.pw_length < 3:
            self.required_flags &= ~gf.Uppercase
        if self.pw_length < 2:
            self.required_flags &= ~gf.Digits
        if gf.Secure in self.flags:
            self.generate_one = self.secure
        else:
            self.generate_one = self.readable

    def secure(self):
        pw = ""
        elements = CONSONANTS_STR
        flags = self.flags
        if gf.Vowels in self.flags:
            elements += VOWELS_STR
        if gf.Uppercase in self.flags:
            elements += elements.upper()
        if gf.Digits in self.flags:
            elements += DIGITS_STR
        if gf.Symbols in self.flags:
            elements += SYMBOLS_STR
        if gf.NoAmbiguous in self.flags:
            elements = "".join(
                char for char in elements if char not in AMBIGUOUS_SET
            )
        for _ in range(self.pw_length):
            char = self.rand.choice(elements)
            if char in DIGITS_STR:
                flags &= ~gf.Digits
            if char in SYMBOLS_STR:
                flags &= ~gf.Symbols
            if char in string.ascii_uppercase:
                flags &= ~gf.Uppercase
            pw += char
        return pw, flags

    def readable(self):
        pw = ""
        first = True
        flags = self.flags
        should_be_consonant = bool(self.rand.randint(0, 1))
        required_flags = gf.Digits | gf.Symbols | gf.Uppercase
        while len(pw) < self.pw_length:
            # Digit case, never start with digit
            if (
                gf.Digits in self.flags
                and not first
                and self.rand.random() > 0.7
            ):
                if gf.NoAmbiguous in self.flags:
                    digit = self.rand.choice(UNAMBIGUOUS_DIGITS)
                else:
                    digit = self.rand.choice(DIGITS_STR)
                flags &= ~gf.Digits
                first = True
                should_be_consonant = bool(self.rand.randint(0, 1))
                pw += digit
                continue

            # Symbol case, never start with symbol
            if (
                gf.Symbols in self.flags
                and not first
                and self.rand.random() > 0.7
            ):
                symbol = self.rand.choice(SYMBOLS_STR)
                flags &= ~gf.Symbols
                first = True
                should_be_consonant = bool(self.rand.randint(0, 1))
                pw += symbol
                continue

            # Vowel and Consonant cases
            if should_be_consonant or gf.Vowels not in self.flags:
                phoneme = self.rand.choice(CONSONANT_PHONEMES)
            else:
                phoneme = self.rand.choice(VOWEL_PHONEMES)

            # Uppercase
            if gf.Uppercase in self.flags and self.rand.random() > 0.8:
                flags &= ~gf.Uppercase
                if len(phoneme) == 1:
                    phoneme = phoneme.upper()
                else:
                    upper_idx = self.rand.randint(0, len(phoneme) - 1)
                    phoneme = (
                        phoneme[0:upper_idx]
                        + phoneme[upper_idx].upper()
                        + phoneme[upper_idx + 1 :]
                    )

            if gf.NoAmbiguous in self.flags and isambiguous(phoneme):
                continue

            should_be_consonant = not should_be_consonant
            first = False
            pw += phoneme
        return pw[: self.pw_length], flags

    def generate(self):
        result = []
        while len(result) < self.num_pw:
            pw, flags = self.generate_one()
            if (flags & self.required_flags) == gf(0):
                result.append(pw)
        return result
