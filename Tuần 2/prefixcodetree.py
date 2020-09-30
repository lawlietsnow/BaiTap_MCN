class PrefixCodeTree:

    def __init__(self, data=None):
        if(data == None): data = -1
        self.left = None
        self.right = None
        self.data = data

    def insert(self, codebook, symbol):
      current = self
      for x in codebook:
        if(x == 0):
          if(current.left is None):
            current.left = PrefixCodeTree(-1)
          current = current.left
        elif(x==1):
          if(current.right is None):
            current.right = PrefixCodeTree(-1)
          current = current.right
      current.left = None
      current.right = None
      current.data = symbol
    
    def decode(self,code,len):
      current = self
      #print(current.left.data)
      binData = BitArray(bytes = code, length=len).bin
      s = ""
      for x in binData:
        if(x == '0'): current = current.left
        elif(x=='1'): current = current.right
        if(current.left is None and current.right is None): 
          s += current.data
          current = self
      print(s)    