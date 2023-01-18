class Component():
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):

    _component: Component = None


    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component


    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"



def client_code(component: Component) -> None:

    print(f"결과 : {component.operation()}", end="")



if __name__ == "__main__":
    test = ConcreteComponent()
    print("아무것도 결합하지 않은 컴포넌트:")
    client_code(test)
    print("\n")

    decorator1 = ConcreteDecoratorA(test)
    decorator2 = ConcreteDecoratorB(decorator1)

    print("데코레이터 결합")
    client_code(decorator2)
