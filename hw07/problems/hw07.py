class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    """

    def __init__(self):
        self.value = 0
        self.prev=1

    def next(self):
        tmpClass=Fib()
        tmp=self.value
        tmpClass.value = self.value + self.prev
        tmpClass.prev=tmp
        return tmpClass

    def __repr__(self):
        return str(self.value)


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self,items,price):
        self.stock_num=0
        self.balance=0
        self.items=items
        self.price=price
    def vend(self):
        if self.stock_num ==0:
            return 'Machine is out of stock.'
        if self.balance<self.price:
            return 'You must deposit ${} more.'.format(self.price-self.balance)
        self.stock_num -= 1
        charge=self.balance -self.price
        self.balance= 0
        if charge!=0:
            return 'Here is your {0} and ${1} change.'.format(self.items,charge)
        else:
            return 'Here is your {0}.'.format(self.items)
    def deposit(self,num):
        if self.stock_num==0:
            return 'Machine is out of stock. Here is your ${}.'.format(num)
        self.balance += num
        return 'Current balance: ${}'.format(self.balance)
    def restock(self,num):
        self.stock_num += num
        return 'Current {0} stock: {1}'.format(self.items,self.stock_num)




class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> double_fussy = MissManners(m) # Composed MissManners objects
    >>> double_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> double_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> double_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> double_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """

    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        "*** YOUR CODE HERE ***"
        mes_split=message.split()
        command=mes_split[1]
        str_space=' '
        if not hasattr(self.obj,command):
            return 'Thanks for asking, but I know not how to {}.'.format(str_space.join(mes_split[1:]))
        else:
            return getattr(self.obj,command)(*args)
