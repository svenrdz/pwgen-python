import pytest
from pwgen_python import Pwgen
from pwgen_python.core import Pwgen, isambiguous, gf


@pytest.mark.parametrize(
    "seed, expected",
    [("seed1", "aingnYnc"), ("seed2", "oinTUinr")],
    ids=["seed1", "seed2"],
)
def test_generate_one_readable(seed, expected):
    pwgen = Pwgen(seed=seed)
    pw, _ = pwgen.readable()
    assert pw == expected


@pytest.mark.parametrize(
    "seed, expected",
    [("seed1", "pHSeutOG"), ("seed2", "frVvFyC3")],
    ids=["seed1", "seed2"],
)
def test_generate_one_secure(seed, expected):
    pwgen = Pwgen(seed=seed)
    pw, _ = pwgen.secure()
    assert pw == expected


def test_no_duplicate():
    pwgen = Pwgen(num_pw=1000)
    passwords = pwgen.generate()
    assert len(set(passwords)) == len(passwords)


@pytest.mark.parametrize(
    "length",
    [0, 100],
)
def test_pw_length(length):
    pwgen = Pwgen(pw_length=length)
    for pw in pwgen.generate():
        assert len(pw) == length


@pytest.mark.parametrize(
    "pw_length",
    [None, -1],
)
def test_pw_length_raises(pw_length):
    with pytest.raises((AssertionError, TypeError)):
        pwgen = Pwgen(pw_length=pw_length)


@pytest.mark.parametrize("num_pw", [0, 100])
def test_num_pw(num_pw):
    pwgen = Pwgen(num_pw=num_pw)
    assert len(pwgen.generate()) == num_pw


@pytest.mark.parametrize(
    "num_pw",
    [None, -1],
)
def test_num_pw_raises(num_pw):
    with pytest.raises((AssertionError, TypeError)):
        pwgen = Pwgen(num_pw=num_pw)


@pytest.mark.parametrize("phoneme, ambiguous", [("uIn", True), ("uin", False)])
def test_isambiguous(phoneme, ambiguous):
    assert isambiguous(phoneme) == ambiguous


@pytest.mark.parametrize(
    "flags", [gf.default(), gf.default() | gf.Secure], ids=["redable", "secure"]
)
def test_ambiguous(flags):
    from pwgen_python.core import AMBIGUOUS_SET

    flags |= gf.NoAmbiguous
    pwgen = Pwgen(flags=flags)
    for pw in pwgen.generate():
        assert len(set(pw) & AMBIGUOUS_SET) == 0


@pytest.mark.parametrize(
    "flags", [gf.default(), gf.default() | gf.Secure], ids=["redable", "secure"]
)
def test_lowercase(flags):
    from string import ascii_uppercase

    flags &= ~gf.Uppercase
    pwgen = Pwgen(flags=flags)
    for pw in pwgen.generate():
        assert len(set(pw) & set(ascii_uppercase)) == 0


@pytest.mark.parametrize(
    "flags", [gf.default(), gf.default() | gf.Secure], ids=["redable", "secure"]
)
def test_symbols(flags):
    from string import punctuation

    flags |= gf.Symbols
    pwgen = Pwgen(flags=flags)
    for pw in pwgen.generate():
        assert len(set(pw) & set(punctuation)) > 0


@pytest.mark.parametrize(
    "flags", [gf.default(), gf.default() | gf.Secure], ids=["redable", "secure"]
)
def test_no_digits(flags):
    from string import digits

    flags &= ~gf.Digits
    pwgen = Pwgen(flags=flags)
    for pw in pwgen.generate():
        assert len(set(pw) & set(digits)) == 0
