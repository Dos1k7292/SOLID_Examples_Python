from abc import ABC, abstractmethod

class IPrinter(ABC):
    @abstractmethod
    def print(self, content: str):
        pass

class IScanner(ABC):
    @abstractmethod
    def scan(self, content: str):
        pass

class IFax(ABC):
    @abstractmethod
    def fax(self, content: str):
        pass

class AllInOnePrinter(IPrinter, IScanner, IFax):
    def print(self, content: str):
        print(f"Printing: {content}")
    def scan(self, content: str):
        print(f"Scanning: {content}")
    def fax(self, content: str):
        print(f"Faxing: {content}")

class BasicPrinter(IPrinter):
    def print(self, content: str):
        print(f"Printing: {content}")

if __name__ == "__main__":
    printer1 = AllInOnePrinter()
    printer1.print("Document")
    printer1.scan("Document")
    printer1.fax("Document")

    printer2 = BasicPrinter()
    printer2.print("Simple Document")
