



class Calculator():

    def summary(self,number):
        return sum(number)

    def minus(self,number):
        return (number[0]-number[1])

    def multiply(self,number):
        return  number[0]*number[1]

    def division(self,number):
        try:
            self.last_number = number[0]/number[1]
        except:
            return 'Недопустимое значение'
        return number[0]/number[1]