from vitamin06 import *
def test_CheckingAccount():
	ch =FreeChecking('Jack')
	ch.balance = 20
	ch.withdraw(3)
	ch.withdraw(100)
	value=ch.withdraw(3)
	assert value==13, "the expected value{0} however got the value{1}".format(13,value)
