import pytest
from pwgen_python import Pwgen


@pytest.mark.parametrize(
    "seed, expected",
    [("seed1", "lFOvypXE"), ("seed2", "dnQqDzB3")],
    ids=["seed1", "seed2"],
)
def test_generate_one(seed, expected):
    pwgen = Pwgen(seed=seed)
    pw = pwgen.generate_one()
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
