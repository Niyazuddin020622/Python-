from random import randint
class Train():

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"Tickets is booked in train no: {self.trainNo} from {fro} to {to} ")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time ")
    def getFare(self,fro,to):
        print(f"Tickets fare in train no: {self.trainNo} from {fro} to {to} is {randint(10000,99999)}")

t = Train(12345)
t.book("islampur","Delhi")
t.getStatus()
t.getFare("islampur","Delhi")
