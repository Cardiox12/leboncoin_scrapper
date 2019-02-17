class LBCHouseProperties(object):
    def __init__(self, price: LBCPrice, rooms: LBCRooms, square: LBCSquare):
        self.price  = price
        self.rooms  = rooms
        self.square = square