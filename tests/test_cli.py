import pytest
from click.testing import CliRunner

from pwgen_python import cli

SEED1 = ["--seed", "seed1"]
SEED2 = ["--seed", "seed2"]

EXPECTED_SEED1 = """
lFOvypXE vZI13W2e bogf7Tnc 4bXvmGac 92qALt1P mxyUhTFd 7Aop2rGq BQjjWJwe
7regcDgi l81XhJW8 zxBvbGxs fJmuX7zO BQcLto5F YmRxNIzC 4tym5Tak MSSVwejI
z9RFVg4D I1xu9Lrx pTQJQ3xD iXCnqkho X9iuvD6K 6oyM0cU6 CL3kimSY RBp8rs2Z
QJOjsiiG hA3kvRbl QH1uiUbs cti5bYCs 0OvF1Z9F e0qnsbkw yUEhY4SX nKpXbx0W
Bm3Iutga l6FuB3Tt 4DiwWW0T jTTGm0v5 2iRILSPz DcyZb7Va yuNOrfhf Nz9P2ipP
QA4TitpS SGt2KAz8 FQl2UUoA if4cPxU8 gD7DmLdk PFzncf9G bbFd4klb dlJRoKmj
tk6SBqnU GkBRGCt8 vYjdqF2Q CDL2GKbm 1ouoDdk1 lAj3o28w jj3nBI39 7CCOKCHs
MWXXf44U cjFmizxg sKxkxurR 1ebvITT9 UldrWERA nr9Win0G 79Al9J4C unBtmYHb
sRpSWbKC hMiuNlpz U1KXUHXI Jhq6BpJR q5f9Fz7c QibtuQfV 7a2VEwz8 3uiUiLZ1
5Sn9MXHD HVvZTtwc Y8wMJPle jEiHkJrs 2YYorB6C mwmQKQHt xP0wz2YT W4Oi8tBC
SWoLjxdx zIqAsXsI 25yHZCa9 1txqvlRR rPtySQhp mx7hWVWy qoaHdz3T pXxPFYjK
XEayIsJ3 WFidOnM3 v7ubHyQE q0BnP79y V67t3f7n 6GZzH67h RQfxhCJM bogrlnLw
SzBNAI91 O4GxLFje 5oymCXvy 2jgh0RGR tacybJjy 4C2rgBLV GR13y0WX 7Ml0Fu2t
8jH23q40 waK1LXqE 7BY8Midb cRgYT0fy LWfcGN0L L0YjsC9U ndhY6KWs IQElg36c
q2bw76fm udLjS7Hp EqoOcXi2 ohXEpoQG sc1Use53 fFGrIjAz 6yWI4umv aR7AhZOC
14OzEZpW MtYn0ija l0wByXD2 wlGzIqGI D92hPJ3W XJBLmT57 dTKNACgc UdO5gxd1
id4wPmOz MsaobX6o rUqxxpY7 NKlpRqIG eHTM6LpW NrDCKqKb jJNozTaj JobxAN2Y
AMMVRI4D UkpehDEB DBughMG2 hNbnjzzV XlvXzvO4 zXOxpoH2 UQPm9DLd mk8yZT68
iWpwc7tR kBP1bOhg brEhJnuX 4wLLfSb5 8CrBqOkO sij9wyZI z48yZNGF AbVnpMag
tjgTdONT fkpdhON7 w8iLbAK5 EJjo6br0 Qx0fURmY JIjep5G9 1vYgCA1K E8zkVzeO
"""

EXPECTED_SEED2 = """
dnQqDzB3 LAJxJfIM tCoUlQmE mNdJdXMq 08Z6snO6 5cJyH3tU l7MpB7AV 1HOixYL4
7WEZdoBL rgRGcJjg f6PNfPKo YBRShe5F TpGIRuB4 lccBNhdj tKDgI4Z4 prcUA7Jg
78k65jYa rilOC4HW OpoONWxw IXCGt85i 4OOz6N5b LaIzXeQO 0kJ2cJA7 nQC9OGlW
GEpwn5SA eocvKuRX xXVkGdLc p5z3ghfn EqGBgPKe J2Mgs5Ya 39fl4o50 cyPh89HY
7kYA2MYb nbwG5zsS js81yZ3T CEyRJjIm t8uhmyEz rIgmPd7l TzvxaxBc MFvrz3cg
jXIFSQsq AmkWXDRt 326m1GyR ArA08og9 YTGK2tgm 0rrZCnRR fsnTXNsD b9YHmjJk
r4V2WEgY 1sgEGatr o0GDUxx8 0Tb09xbr eQT6qOSZ I79EUKtY 0a3aL7Lk 74ncYBTm
Frv33o6Z HbKtp9nW 47N8qK9N rQM4hxU5 VPkG14Eq ocyMIrii zGXV9pIC DYntJer6
RNhixicD YhWn4UDl Ozpf06B0 NSGXvwUa SqHjPZBo bnvBuUA4 K2G2SeeB 6y1cJjIC
qL0OzNww 7sa2Rtkx 6skSuJ5z QMMLPu7i 5fh8ULj8 0w70sUEf anZGYyTa WNO9ShKB
kobMYISE tbeQGcCw giJxmEhh nm0dMurU 48DJJMO2 lZmK5b4W 7Srcxjm5 iOKOfyyC
ITcHu2hO xDR3cPiE k9iGWneu waEuGolJ KDoMM3fP lPx749Hw lh2sVoYK DoZk98x1
0edpL4iE 6wReebp0 1EQVr98R Fk9AoNsV XY9Ns9r8 fSenyYWb DNMErAxR JwFWEVrN
yCDOG1qR 8b0bQ3WZ dBZ5DkJd dSpJA67e Huxl09Zu 2uVVXbno Q7vM0gtS InIMkK29
vxycCqu0 lHKK03aW mkzcQJyP 5jht94Rv HLyx8Aiq y3HC4epK qjEMcsIX yucjP6nB
ZbtU5vlD qIenPXzu iBs49g03 dUGSU2IF alww1zJy lold8Jl2 mGDcINtW jis2rEYB
M4a4TN9V iT9qrC5F TSzw9Fh6 XMEIDSiJ SK33j5QT Wr1cUali Q13X6Feg LwBUIDRy
Tge9ct5U hb4mjs1r JCikgrpp o3srsgZA F1IUgja1 x4VukJXT JuxMC9PT TL5BB8Aw
vDjnBqI4 CvG1yvQF Eavtw8oF b3DaMO1B OyIbS6gD epeQA1uA mHDSNMoU 6ljP3zoi
E1pKbUQ9 HbRjymgD Sl5jGEdc QqrmyYFJ krJ2vjE3 w5LnJrYA nLvPyFgg FIi8ouOL
"""


def enum_output(output: str) -> list[tuple[int, str]]:
    output_list = output.replace(" ", "\n").split()
    for i, pwd in enumerate(output_list):
        yield i, pwd


def split_output(output: str) -> list[str]:
    for i, pwd in enum_output(output):
        yield pwd


@pytest.mark.parametrize(
    "seed, expected_output",
    [(SEED1, EXPECTED_SEED1), (SEED2, EXPECTED_SEED2)],
    ids=["seed1", "seed2"],
)
def test_no_args(seed, expected_output):
    runner = CliRunner()
    result = runner.invoke(cli, seed)
    assert result.exit_code == 0
    for pwd, expected in zip(
        split_output(result.output), split_output(expected_output)
    ):
        assert pwd == expected
