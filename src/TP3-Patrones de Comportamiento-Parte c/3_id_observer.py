from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
import random
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    _id: int = None  #id

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nSubject: I'm doing something important.")
        self._id = random.choice([1234,9011,5678,2223,4433,5234,9943,1112])

        print(f"Subject: My id has just changed to: {self._id}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._id ==1234:
            print("ConcreteObserverA: Los ids coinciden")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._id ==9011:
            print("ConcreteObserverB: Los ids coinciden")

class ConcreteObserverC(Observer):
    def update(self, subject: Subject) -> None:
        if subject._id ==4433:
            print("ConcreteObserverC: Los ids coinciden")

class ConcreteObserverD(Observer):
    def update(self, subject: Subject) -> None:
        if subject._id ==1112:
            print("ConcreteObserverD: Los ids coinciden")


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    observer_c = ConcreteObserverC()
    subject.attach(observer_c)

    observer_d = ConcreteObserverD()
    subject.attach(observer_d)

    subject.some_business_logic()
    subject.some_business_logic()
    subject.some_business_logic()
    subject.some_business_logic()

    
