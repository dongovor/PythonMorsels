class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    
    def __repr__(self):
        '''return readable representation of this point'''
        return f"Point(x={self.x}, y={self.y}, z={self.z})"
    
    def __eq__(self, other):
        '''return true if point is equal to other point'''
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self, other):
        '''return copy of point, shifted by other'''
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        '''return copy of point, shifted by other'''
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)
