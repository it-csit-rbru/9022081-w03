from Building import Building
class Room:
    code:str
    building:Building
    floor:str
    seat:int
    def __init__(self,code,building,floor,seat) -> None:
        self.code = code
        self.building = building
        self.building.addRoom(self)
        self.floor = floor
        self.seat = seat
    def __str__(self) -> str:
         return f"ห้อง {self.code} อาคาร {self.building.name} ชั้น {self.floor} รองรับ {self.seat} ที่นั่ง"