class Target:
    def request(self) -> str:
        return "Target: 타겟의 기본 행동입니다."

class Adaptee:
    def specific_request(self) -> str:
        return "specific behavior"

class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f'Adapter: (TRANSLATED) {self.specific_request()[::-1]}'


def client_code(target: "Target") -> None:
    print(target.request(), end="")


if __name__ == '__main__':
    print("Client: I can work just fine with the Target object")
    target = Target()
    client_code(target)
    print("")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface,"
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
