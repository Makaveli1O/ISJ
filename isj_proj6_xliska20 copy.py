"""Do souboru, nazvaného podle konvence isj_proj6_xnovak00.py, implementujte třídu Polynomial, která bude pracovat s polynomy reprezentovanými pomocí seznamů. Například 2x^3 - 3x + 1 bude  reprezentováno jako [1,-3,0,2] (seznam začíná nejnižším řádem, i když se polynomy většinou zapisují opačně).

Instance třídy bude možné vytvářet několika různými způsoby:
pol1 = Polynomial([1,-3,0,2])
pol2 = Polynomial(1,-3,0,2)
pol3 = Polynomial(x0=1,x3=2,x1=-3)

Volání funkce print() vypíše polynom v obvyklém formátu:
>>> print(pol2)
2x^3 - 3x + 1

Bude možné porovnávat vektory porovnávat:
>>> pol1 == pol2
True

Polynomy bude možné sčítat a umocňovat nezápornými celými čísly:
>>> print(Polynomial(1,-3,0,2) + Polynomial(0, 2, 1))
2x^3 + x^2 - x + 1
>>> print(Polynomial(-1, 1) ** 2)
x^2 - 2x  + 1

A budou fungovat metody derivative() - derivace a at_value() - hodnota polynomu pro zadané x - obě pouze vrací výsledek, nemění samotný polynom:
>>> print(pol1.derivative())
6x^2 - 3
>>> print(pol1.at_value(2))
11
>>> print(pol1.at_value(2,3))
35
(pokud jsou zadány 2 hodnoty, je výsledkem rozdíl mezi hodnotou at_value() druhého a prvního parametru - může sloužit pro výpočet určitého integrálu, ale ten nemá být implementován)
"""


class Polynomial:
    def __init__(self,*args,**kwargs):
        self.polynomial_list=list() #vytvorenie prázdneho listu
        
        for i in args:
            if type(i) is list: #ak je vložený list už na začiatku, nemusíme konvertovať a máme požadovaný formát
                self.polynomial_list=i
            else:
                self.polynomial_list.append(i) #ak argument nieje list, appendujem prázdny list argumentami

        
        # prevencia proti zapisovaniu mimo indexov listu
        for key, item in kwargs.items():
            index = int(key.split('x')[1]) #-> ziskanie indexu

            if len(self.polynomial_list) > index: # ak je list dostatočne veľký, priradím
                self.polynomial_list[index] = item
            else: #ak list nieje dostatočne veľký musimé nulovať k indexu
                for i in range(index+1-len(self.polynomial_list)):
                    self.polynomial_list.append(0)
                self.polynomial_list[index] = item #priradenie indexu
        
        #nulované položky je potrebné následne zmazať
        for i in range(len(self.polynomial_list)-1, 0, -1):
            if self.polynomial_list[i] == 0:
                del self.polynomial_list[i]
            else:
                break

    def __str__(self): # -> "to string"
        pol_len = len(self.polynomial_list)
        temp_str = ''
        if pol_len == 1: # dlzka musi byt vacsia ako 1
            temp_str = temp_str + str(self.polynomial_list[0])
            return temp_str
        
        for i in range(pol_len-1):# -> polynom z listu
            if self.polynomial_list[pol_len-i-1] != 0:
                if self.polynomial_list[pol_len-i-1] > 0:
                    if len(temp_str) != 0:
                        temp_str += ' + '
                else:
                    temp_str += ' - '

                if abs(self.polynomial_list[pol_len-i-1]) != 1:
                    temp_str += str(abs(self.polynomial_list[pol_len-i-1]))

                temp_str += 'x'

                if pol_len-i-1 > 1:
                    temp_str += '^' + str(pol_len-i-1)
        if self.polynomial_list[0] != 0:
            if self.polynomial_list[0] > 0:
                temp_str += ' + ' + str(self.polynomial_list[0])
            else:
                temp_str += ' - ' + str(abs(self.polynomial_list[0]))
        #add 0 to string if it is still empty after creating regular format of polynomial
        if len(temp_str) == 0:
            temp_str = '0'
        return temp_str


#TIETO ESTE PREPISAT



    def __eq__(self, other):

        # if they're same class
        if isinstance(self, other.__class__):
            # if their internal list match
            if self.polynomial_list == other.polynomial_list:
                return True
        return False

    def __add__(self, other):
        arr = list()
        #recognise shortest and lonfest list
        if len(self.polynomial_list) < len(other.polynomial_list):
            shortest = len(self.polynomial_list)
            longest = other.polynomial_list
        else:
            shortest = len(other.polynomial_list)
            longest = self.polynomial_list
        #add in list n items (n=length of shorter polynomial}
        for i in range(shortest):
            arr.append(self.polynomial_list[i]+other.polynomial_list[i])
        #add in the end of the list items to length of longest polynomial
        for i in range (len(longest) - shortest):
            arr.append(longest[shortest+i])
        return Polynomial(arr)

    def __radd__(self, other):
        arr = list()
        #recognise shortest and lonfest list
        if len(self.polynomial_list) < len(other.polynomial_list):
            shortest = len(self.polynomial_list)
            longest = other.polynomial_list
        else:
            shortest = len(other.polynomial_list)
            longest = self.polynomial_list
        # add in list n items (n=length of shorter polynom}
        for i in range(shortest):
            arr.append(self.polynomial_list[i] + other.polynomial_list[i])
        #add in end of the list items to length of longest polynom
        for i in range(len(longest) - shortest):
            arr.append(longest[shortest + i])
        return Polynomial(arr)

    def __mul__(self, other):
        #inicialize list
        arr = [0]*(len(self.polynomial_list) + len(other.polynomial_list) + 1)
        for i in range(len(self.polynomial_list)):
            for k in range(len(other.polynomial_list)):
                arr[i+k] += self.polynomial_list[i]*other.polynomial_list[k]
        return Polynomial(arr)

    def __pow__(self, power):
        if power > 1:
            arr = self
            for i in range(1,power):
                arr = arr*self
            return arr
        #if power is 1 return orignal polynomial
        elif power == 1:
            return Polynomial(self.polynomial_list)
        #if power is 0 return 1 (everything powered by 0 is 1)
        elif power == 0:
            return 1
        #return error if power is negative
        else:
            raise ValueError("SORRY, I KNOW IT SHOULD WORK, BUT MY PROJECT ASSIGMENT DOESN'T ALLOW IT")

    def derivative(self):
        length = len(self.polynomial_list)
        #if length is 1 is not polynomial just number
        if length == 1:
            return 0
        else:
            arr = list()
            for i in range(length):
                arr.append(self.polynomial_list[i]*(i))
            #delete first item from list, because it is redundant and equal 0
            arr.pop(0)
            return Polynomial(arr)

    def at_value(self, num1, num2='x'):
        result = 0
        #execution of value of polynomial for particular x (when in input is only 1 parameter)
        if num2 == 'x':
            result = self.polynomial_list[0]
            for i in range(1,len(self.polynomial_list)):
                sum = num1
                for k in range(i-1):
                    sum = sum*num1
                result = result + self.polynomial_list[i]*sum
            return result
        #value after subtraction 2 results when in input are 2 particular value of x
        else:
            result1 = self.polynomial_list[0]
            result2 = self.polynomial_list[0]
            for i in range(1, len(self.polynomial_list)):
                sum1 = num1
                sum2 = num2
                for k in range(i - 1):
                    sum1 = sum1 * num1
                    sum2 = sum2 * num2
                result1 = result1 + self.polynomial_list[i] * sum1
                result2 = result2 + self.polynomial_list[i] * sum2
            result = result2-result1
            return result




def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()
