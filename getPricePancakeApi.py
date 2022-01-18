import sys
import requests
from web3 import Web3
from getPricePancake import calcApi

if len(sys.argv) > 1:
    COIN = str(sys.argv[1])
else:

    help = """
    BNB = 0x86662228d0e24a5498db862cf36031d9f1e0e254
    CAKE = 0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82
    BCOIN = 0x00e1656e45f18ec6747f5a8496fd39b50b38396d
    PACOCA = 0x55671114d774ee99d653d6c12460c780a67f1d18
    CCAR = 0x50332bdca94673f33401776365b66cc4e81ac81d
    CPAN = 0x04260673729c5f2b9894a467736f3d85f8d34fc8
    CGUARD =

    """
    print(help)
    COIN = input('Enter Contract: ')

print('API', calcApi(COIN))
