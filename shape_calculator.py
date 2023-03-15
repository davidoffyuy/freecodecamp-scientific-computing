class Rectangle:
    height = ""
    width =""
    
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)
    
    def __str__(self):
        ret_str = "Rectangle(width={0:d}, height={1:d})"
        return ret_str.format(self.width, self.height)

    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width* self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_amount_inside(self, comp_rect):
        # Checking to see if shape is too big to fit at all on either sides
        if comp_rect.width > self.width:
            return 0
        elif comp_rect.height > self.height:
            return 0
        
        # Calculate how many can fit in each dimension
        x_fit = int(self.width / comp_rect.width)
        y_fit = int(self.height / comp_rect.height)
        return x_fit * y_fit
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        ret_str = ""
        for i in range(self.height):
            for j in range(self.width):
                ret_str += "*"
            ret_str += "\n"
        
        return ret_str
                


class Square(Rectangle):
    def __init__(self, side):
        self.set_side(side)

    def __str__(self):
        ret_str = "Square(side={0:d})"
        return ret_str.format(self.width)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side
        
    def set_height(self, side):
        self.width = side
        self.height = side