class WalletFunctor:
    def __init__(self, startCoins=100):
        self.__startCoins = startCoins

    def __call__(self, coins=0):
        return self.__startCoins + coins


class UserPlayer:
    def __init__(self, name):
        self.name = name
        self.__walletSetter = WalletFunctor()
        self.__wallet = self.__walletSetter()

    def updateWallet(self, coins=0):
        self.__wallet = self.__walletSetter(coins)

    def showWallet(self):
        print(f"{self.name}! You have {self.__wallet} coins now.")


user1=UserPlayer("Joe")
user1.showWallet()
user1.updateWallet(50)
user1.showWallet()
