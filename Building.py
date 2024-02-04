class Building :
    name:str
    code:str
    roomList = []
    def __init__(self,name,code) -> None:
        self.name = name
        self.code = code
    def addRoom(self,room):
        self.roomList.append(room)
    def printAllRoom(self):
        for room in self.roomList:
            print(room)
    def __str__(self) -> str:
        return f"{self.name}({self.code})"
    
    