###https://youtu.be/Xoq5vHYPpUM  (codeyug)
class Roman:
    def calculate(self,s):
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

        i=0
        num=0

        while i<len(s) :
                if s[i:i+2] in d and  i<=len(s):
                    num+=d[s[i:i+2]]
                    i+=2

                else:
                    num+=d[s[i]]
                    i+=1
        return  num



r=Roman()
print(r.calculate("CDXLIII")) #443
print(r.calculate("III"))