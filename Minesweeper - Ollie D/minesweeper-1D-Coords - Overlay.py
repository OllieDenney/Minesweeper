from tkinter import *
import random
import sys
print(sys.getrecursionlimit())     

sys.setrecursionlimit(2500)

"""
    Limit number of mines to 20
    
    If user clicks mine - game end
    If user clicks number - only show number
    If user clicks blank square - show all near blank squares
"""

class Framebuild():

    def __init__(self, *args, **kwargs):
        # Setup Canvas
        self.c = Canvas(root, height=400, width=250, bg='white')
        self.c.pack(fill=BOTH, expand=True)

        frame1 = Frame(self.c)
        frame1.pack(side='top')

        self.c.bind('<Configure>', self.createGrid)
        self.pixel_width = 20
        self.pixel_height = 20

        # Setup binds
        self.c.bind("<ButtonPress-1>", self.leftClick)

        self.menu = Canvas(root, height = 400, width = 250, bg='white')
        self.menu.pack()
        self.c.pack(fill=BOTH, expand=True)
        self.new_game_button = Button(root, text = "New Game", command = self.new_game)
        self.new_game_button.pack()

        self.mine_scale = Scale(root, orient=HORIZONTAL, sliderlength = 15, from_=1, to=20, label="Mine Amount:")
        self.mine_scale.pack()

        frame2 = Frame(self.menu)
        frame2.pack(side='bottom')

    def leftClick(self, event):
        items = self.c.find_closest(event.x, event.y)
        print(event.x, event.y)
        if items:
            rect_id = items[0]
            self.c.itemconfigure(rect_id, fill="red")
            print(rect_id)
            self.on_click_decision(rect_id)
    """
        def on_click_decision(self, rect_id):
        for i in 
        if rect_id in mine_coords:
            print("dead, kaboom")
    """



    def createGrid(self, c):
        for x in range(0, 10):
            for y in range(1, 11):
                x1 = (x * self.pixel_width)
                x2 = (x1 + self.pixel_width)
                y1 = (y * self.pixel_height)
                y2 = (y1 + self.pixel_height)
                self.c.create_rectangle(x1,y1,x2,y2)
            self.c.update()
    
    def new_game(self):
        mine_amount = self.mine_scale.get() #Need to add a confirm mine amount button
        mine_coords = []
        for i in range(mine_amount):
            self.mine_placement()
            mine_coords.append(self.mine_coord)
        print(mine_coords)
        self.number_generation(mine_coords)


    def mine_generation(self):
        final_coord = random.randint(1, 99)
        return final_coord

    def mine_placement(self):
        self.mine_coord = self.mine_generation()
        self.c.itemconfigure(self.mine_coord, fill="yellow")
        return self.mine_coord

    def coord_splitter(self, coord):
        print("Coord Splitter:")
        print("Og:", coord)
        coord = str(coord)
        coords = []
        if int(coord) < 10:
            y_coord = coord
            x_coord = 0
        elif int(coord) == 10:
            y_coord = 10
            x_coord = 0
        else:
            for char in coord:
                coords.append(char)
            print(coords)
            x_coord = coords[0]
            coords.remove(coords[0])
            y_coord = ""
            for char in coords:
                y_coord += char
        print(y_coord)
        print("Processed:",x_coord, y_coord)
        return(x_coord, y_coord)

    def number_generation(self, mine_coords):
        mine_data_list = []
        for coord in range(1, 101):
            if coord not in mine_coords:
                mine_data = []
                mines_prox = self.proximity_check(coord, mine_coords)
                if mines_prox == 0:
                    print("run the big boy function")
                if mines_prox == 1:
                    mine_data.append(coord)
                    mine_data.append(1)
                if mines_prox == 2:
                    mine_data.append(coord)
                    mine_data.append(2)
                if mines_prox == 3:
                    mine_data.append(coord)
                    mine_data.append(3)
                if mines_prox == 4:
                    mine_data.append(coord)
                    mine_data.append(4)
                if mines_prox == 5:
                    mine_data.append(coord)
                    mine_data.append(5)
                if mines_prox == 6:
                    mine_data.append(coord)
                    mine_data.append(6)
                if mines_prox == 7:
                    mine_data.append(coord)
                    mine_data.append(7)
                if mines_prox == 8:
                    mine_data.append(coord)
                    mine_data.append(8)
            mine_data_list.append(mine_data)
        print(mine_data_list)
        print(len(mine_data_list))


    
    def proximity_check(self, coord, mine_coords):
        nums = self.coord_splitter(coord)
        x_coord = nums[0]
        y_coord = nums[1]
        print(x_coord)
        print(y_coord)
        total_mines_in_prox = 0
    
        print(mine_coords)

        #Function is very long, could possibly take code after coord 
        #processing and put into a method or possibly a class

        proximity_coords = [-1, -11, -10, -9, 1, 11, 10, 9]
        proximity_coords_top = [-10, -9, 1, 11, 10]
        proximity_coords_bottom = [-1, -11, -10, 10, 9]

        if y_coord == "1":
            for i in range(5):
                updated_coord = coord + proximity_coords_top[i]
                print("Updated Coord:", updated_coord)
                for mine_coord in mine_coords:
                    if mine_coord == updated_coord:
                        total_mines_in_prox += 1
                        break
        elif y_coord == "0":
            for i in range(5):
                updated_coord = coord + proximity_coords_bottom[i]
                print("Updated Coord:", updated_coord)
                for mine_coord in mine_coords:
                    if mine_coord == updated_coord:
                        total_mines_in_prox += 1
                        break
        else:
            for i in range(8):
                updated_coord = coord + proximity_coords[i]
                print("Updated Coord:", updated_coord)
                for mine_coord in mine_coords:
                    if mine_coord == updated_coord:
                        total_mines_in_prox += 1
                        break

        print(total_mines_in_prox)
        return total_mines_in_prox




root = Tk()
gui = Framebuild(root)
root.geometry("250x290+0+0")
root.mainloop()