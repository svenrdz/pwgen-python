# Pwgen

[pwgen](https://linux.die.net/man/1/pwgen) made with python

```
› pwgen-python
e9IqfCzy ZDkjBKx9 XploKifG vtYyn2ly Sk5DNhEA M7uhXfbb XI67Jvvk Iewbw1nX
ohdQrbhw 6BQDso2A 9Q2JAD6o zwbWf64H 6moVvIFL 6weW4yB0 HoCX4XSi kacVCd42
J0lJo6mX 9EfjR2oq TLhUjwaD HD6JjV1n ZwDLpxOw 1Y9t5Mw1 HLNRXIyH IF3wMgyu
AQyNbFjV YHQlqJh5 Iy3NRXee d2kV9yJs FVPZMPLS pd4VMLZd 7lsNAnyF jMIu4NhS
cEZ7LL9y W7uUuzMA zCKUhpiy HC0KeLIh ZNu7m0um 1my7MvCu 9bMBuw3u O7PCE1ig
73eVvPhR 8wbgHZ47 MpAbtYfW uQOoJNrX MlCOcNR9 K3DV9Hlx dILPbOac 21u5rGq9
ljIVH0Fw HziQcpmn Je0RkrT0 Wnk7F97v wZ6V8pBx bq6dT0D8 faxaSUbX Jpr5ypqN
Fag4bSTm OU07sU9P PoLeu7iE h9GZGCTW Ti07HNOg 7TDql2UN 4tnEn4hk JHRYPBKt
u7w6gCUU KvhQ7exf L1du3P6x cioH36yL koHe9ufj BVu3WTnJ cKSh9l58 NZZ0boxM
Z3s8lXsT rE0fDKWo f6Wtyrk5 SEY26YSn BmsvrwBf BI6WjNMO EX6UV0vZ FaRxOIj3
7gvDv8TU KUoIGZFe rUerII9W EcSKgGp7 3Q2sJ1vl Qdbf5HwZ 2h6aXajZ wrNLnLnh
7osyFwOZ ZmiBeYGU G8xVo55f GhS8kzIC Q7cyzBpy OWws5ByU KrbE6Utt iYtIdGbg
roFRdtOy mfsJAqBZ VCCAc7QU A1lwA0HJ JdMeLysk AIK2WJBX DTq31QPN 09tiyDIJ
OtlFFjyA luM7SorX WTN9LCLz Yi5Da436 cpwzrt6E iWVeMmbD VXwQtPXW kGel5bUo
XG12D9DN Expq6z7b J4m6JKKG JM7c89ip Jz3c5RvG 2REINrqY sMArGt2A VnNnCwJ1
WxFTmAUZ e4eWrdBm w1NsnY5x H6KbdK8e vlQSS9Ze fnti4DUP YfVvAqkV UKtNnxgX
ocCIKh30 vRmj5LkE pdZZlJZm x23CnWGw sABuMSE0 JCPNigJK QYUEa5Fo gc0VnH6A
ROcffHmJ zi32Py0j ACHTz4UH zlWNB4XW ooumZ0Yf 8RMBI8zj AYv9O8qQ UmvyPC66
3hVVkgOv BzmDgX90 3BcABFoa hNejMWCD BW2XgDbl OJLtM8Wt rXCg319r 40os00px
V3cUmZYB UgWITcrZ NduWkOFD RZ4eZy8G 8pnSKbUu llWvB2JI Z7rljDBl EaAJrS78
```

## Installation

Using pip:
```
pip install .
```

## Usage

```
Usage: pwgen-python [OPTIONS] [PW_LENGTH] [NUM_PW]

Options:
  -N, --num-passwords INTEGER
  -H, --sha1 SHA1
  -S, --seed TEXT
  -h, --help                   Show this message and exit.
```

## Testing

```
› make test
pytest --cov=. --cov-report term-missing tests/
============================ test session starts =============================
platform darwin -- Python 3.9.1, pytest-6.2.5, py-1.11.0, pluggy-0.13.1
rootdir: /Users/sven/ws/dalibo/pwgen-python
plugins: anyio-2.2.0, web3-5.19.0, cov-3.0.0
collected 26 items

tests/test_cli.py ...............                                      [ 57%]
tests/test_core.py ...........                                         [100%]

---------- coverage: platform darwin, python 3.9.1-final-0 -----------
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
pwgen_python/__init__.py      50      1    98%   81
pwgen_python/core.py          25      0   100%
pwgen_python/utils.py         18      1    94%   27
setup.py                       2      2     0%   1-3
tests/__init__.py              0      0   100%
tests/test_cli.py             92      0   100%
tests/test_core.py            28      0   100%
--------------------------------------------------------
TOTAL                        215      4    98%


============================= 26 passed in 0.09s =============================
```
