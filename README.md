# Pwgen

[pwgen](https://linux.die.net/man/1/pwgen) made with python

```
› pwgen-python
aiC6ueur R0umkum4 r9thuiL0 Ouf3uer1 iEVueus3 intH5Iph iE1wy7ca rrUe0c6g
douaJyn5 T6tho5ou noi7uIti PoiphAi8 T6gnongu DoIjem9c w0IlAKoi Ancr4ons
l3ua8f0i ym6iGnuc ainNg9im einciE6v ougN1k1f ueusCue8 zEptuIn5 emL6si2s
P9NneuL6 tuI9aunu Pt6Deu1a anph8gnO ph0L0Cue an9C9r2e S6sSienp Ai7Lain8
Oiwueu1f oI0untho entron4Q scuaNch2 USu3Y2ea aN4puasc scinb7eU e3uAn2sH
i5yNnein Ymreum6a cimt4uEu tIeuTh5C vem6Bin6 c6Ss0onn fFym8ng9 cr1Rrozo
Uch5invo jysSia7v mm7ainTe ieutrY9u ss2ie6nu ttEau3ou iM9rhien mAngieu4
guiN3ach scU8yd1m b5aDiemm Ua0jon5j lutHeml4 th9ymtTi oI8gnoua yN0zieme
uiNkanw3 WOtr1abu o5N8iEuB oi3iN5nn aiNB6umd BAim7nga Trua0kei an9trOu0
cueng5U3 uerK5ren v6AmynQu Aiph3c2i ein4mYpi cRumss4U ir7tI7cR Ch4cymsh
c3anSimn r1oI6e8y ussim4yN anRrI4i8 oU2gnaij ng7ss7Mo w5umcuNf zIeff0ty
uerR0Chi fFun3mmi sSeau9ue oi3sHan8 ycAn8mma gnoTA8rh uin6piAv eNniap8u
qu3aNbou d1ia4M6s eph7unTh cUzi6aim uancRy2u quek6AiV ym4pienN buanph1M
Eu2cH5se faiph4Ui ch3nueRc qu3neAu3 s6OuDUan Chuin9ie eau1Inna Cieu8onp
mm5eaUng N9ymph1k t7s3F9em Ffein5gn traIm7ch zaiKeu9u sSym2yns ie9Tian1
syn8Aiju jynm4Vum Quienmm0 esieUch6 Emj8scai F2f3uing aUth3man criNf3tr
InS1cieu puas8P9s ouatr1Ua Muinnyn4 diMm4ems R8noU8ia att0boP4 y5luaqUu
uatOid3g eumeucR5 k4qU7j0o n0tYn0ie r7gn1Pta ynpt7uiS creRr6ui iendaI8u
beIns1sc sh2eAc9u a5Ua1y0e em8uN8ai sc5Umss6 yMthien8 e0rR4uer un9oI5f5
quYn0thy Au2b6n0s Iaz0ai0a shanG2Z8 Ph9oUsua Ffoin0pa tTen3uth eammeaU6
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
  -N, --num-passwords INTEGER     Number of generated passwords. Lower
                                  precedence than `NUM_PW`

  -1                              Generate 1 password.
  -S, --seed TEXT                 Seed from string.
  -H, --sha1 /PATH/TO/FILE[#SEED]
                                  Seed from file. Optional string seed after #
  -C, --columns / -L, --line      Output format. [default: columns]
  -s, --secure / -r, --readable   Enable/disable secure password generation.
                                  [default: readable]

  -V, --vowels / -v, --no-vowels  Enable/disable use of vowels. [default:
                                  vowels]

  -D, --digits / -d, --no-digits  Enable/disable use of digits. [default:
                                  digits]

  -u, --uppercase / -l, --lowercase
                                  Enable/disable use of uppercase letters.
                                  [default: uppercase]

  -y, --symbols                   Enable use of symbols. [default: False]
  -a, --no-ambiguous              Disable use of ambiguous characters.
                                  [default: False]

  -h, --help                      Show this message and exit.
```

## Testing

```
› make
pytest --cov=. --cov-report term-missing tests/
============================= test session starts ==============================
platform darwin -- Python 3.9.1, pytest-6.2.5, py-1.11.0, pluggy-0.13.1
rootdir: /Users/sven/ws/dalibo/pwgen-python
plugins: anyio-2.2.0, web3-5.19.0, cov-3.0.0
collected 47 items

tests/test_cli.py ........................                               [ 51%]
tests/test_core.py .......................                               [100%]

---------- coverage: platform darwin, python 3.9.1-final-0 -----------
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
pwgen_python/__init__.py      69      3    96%   140, 142, 150
pwgen_python/core.py         102      0   100%
pwgen_python/utils.py         29      0   100%
setup.py                       2      2     0%   1-3
tests/__init__.py              0      0   100%
tests/test_cli.py             98      0   100%
tests/test_core.py            65      0   100%
--------------------------------------------------------
TOTAL                        365      5    99%


============================== 47 passed in 0.34s ==============================
```
