#@Author: Jared Campbell
#Date: 06/15/22

class Currency:

    def __init__(self,country,symbol,l_or_r,c_or_d,amount):
        self._country = country
        self._symbol = symbol
        self._l_or_r = l_or_r
        self._c_or_d = c_or_d
        self._amount = amount
    def isValid(self):
        if self._c_or_d == 'comma':
            self._c_or_d = False
        else:
            self._c_or_d = True
        if self._l_or_r == 'left':
            self._l_or_r = True
        else:
            self._l_or_r = False


   
    def __str__(self):
        if self.isValid():
            if self._l_or_r == True:
                return "{0:s}{1:,.2f}".format(self._symbol , self._amount)
            else:
                return "{0:,.2f}{1:s}".format(self._amount, self._symbol)
        else:
            if self._l_or_r == True:
                valid = "{0:s}{1:,.2f}".format(self._symbol,self._amount)
                valid = valid.replace(",", "temp")
                valid = valid.replace(".",",")
                valid = valid.replace("temp", ".")
                return valid
            else:
                valid = "{0:,.2f}{1:s}".format(self._amount, self._symbol)
                valid = valid.replace(",", "temp")
                valid = valid.replace(".",",")
                valid = valid.replace("temp", ".")
                return valid