
"""
폴더구조

GeneralManager
        Manager1
            Developer11
            Developer12
        Manager2
            Developer21
            Developer22
"""

class LeafElement:
    def __init__(self, *args):
        self.position = args[0]
  
    def showDetails(self):
        print("\t", end ="")
        print(self.position)
  
  
class CompositeElement:
    def __init__(self, *args):
        self.position = args[0]
        self._children = []
  
    def add(self, child):
        self._children.append(child)
  
    def remove(self, child):
        self._children.remove(child)
  
    def showDetails(self):
        print(self.position)
        for child in self._children:
            print("\t", end ="")
            child.showDetails()
  
  
"""main method"""
  
if __name__ == "__main__":
    """최상위 폴더 생성 """
    topLevelMenu = CompositeElement("GeneralManager")

    """Manager1, 2 폴더 생성"""
    subMenuItem1 = CompositeElement("Manager1")
    subMenuItem2 = CompositeElement("Manager2")

    """Manager 폴더에 들어갈 파일 생성"""
    subMenuItem11 = LeafElement("Developer11")
    subMenuItem12 = LeafElement("Developer12")
    subMenuItem21 = LeafElement("Developer21")
    subMenuItem22 = LeafElement("Developer22")

    """Manager 폴더에 Developer파일 add"""
    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem2.add(subMenuItem21)
    subMenuItem2.add(subMenuItem22)
    
    """Manager폴더 두개를 최상위 GeneralManager폴더에 집어넣음"""
    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    
    topLevelMenu.showDetails()
