from __future__ import annotations
from abc import ABC, abstractmethod

# Button 인터페이스
class Button(ABC):
    
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self):
        pass

#Button 인터페이스를 상속받는 구상제품 
class HtmlButton(Button):
    '''
        other code...
    '''
    def render(self) -> None:
        print("render : HtmlButton!!")

    def on_click(self) -> None:
        print("Click HtmlButton !!")


class WindowButton(Button):
    '''
        other code...
    '''
    def render(self) -> None:
        print("render : WindowButton!!")

    def on_click(self) -> None:
        print("Click WindowButton !!")



class Dialog(ABC):
    
    def render_window(self):
        _button = self.create_button()
        _button.render()

    @abstractmethod
    def create_button(self) -> Button:
        pass
    


class HtmlDialog(Dialog):
    def create_button(self) -> Button:
        return HtmlButton()


class WindowDialog(Dialog):
    def create_button(self) -> Button:
        return WindowButton()


def configure(name: str):
    # Html 아니면 모두 윈도우 버튼으로 가정
    return HtmlDialog() if name == "Html" else WindowDialog()


def run_business_logic(dialog: Dialog):
    dialog.render_window()


if __name__ == "__main__":
    
    dialog: Dialog = configure("Html")
    run_business_logic(dialog)

    dialog = configure("Window")
    run_business_logic(dialog)

