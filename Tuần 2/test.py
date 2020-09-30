from prefixcodetree import *
codeTree=PrefixCodeTree()
codebook = {
    'x1': [0],
    'x2': [1,0,0],
    'x3': [1,0,1],
    'x4': [1,1]
}
for symbol in codebook:
  codeTree.insert1(codebook[symbol], symbol)
codeTree.decode(b'\xd2\x9f\x20',21)