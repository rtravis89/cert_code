class Rectangle:
    def __init__(self,width,height):
        self.height = height
        self.width = width

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"    

    def set_height(self,height):
        self.height = height
        return None

    def set_width(self,width):
        self.width = width
        return None

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2*self.height + 2*self.width

    def get_diagonal(self):
        return (self.height**2 + self.width**2)**(.5) 

    def get_picture(self):
        picture = ""
        if self.width >= 50 or self.height >= 50:
            picture = "Too big for picture."
        else:    
            for i in range(0,self.height):
                picture += "*"*self.width + "\n"
        return picture    

    def get_amount_inside(self, rectangle):
        height_fit = int(self.height / rectangle.height)
        width_fit = int(self.width / rectangle.width)
        return height_fit*width_fit



class Square(Rectangle):
    def __init__(self, width):
        self.width = width
        self.height = width
        super().__init__(width,width)

    def __str__(self):
        return f"Square(side={self.width})"    

    def set_side(self,side):
        self.width = side
        self.height = side
        return None

    def set_width(self,width):
        self.width = width
        self.height = width
        return None

    def set_height(self,height):
        self.width = height
        self.height = height
        return None        

