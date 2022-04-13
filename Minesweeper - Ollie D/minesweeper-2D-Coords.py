from tkinter import *
import random
import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(2500)

class Framebuild():

    def __init__(self, *args, **kwargs):
        # Setup Canvas
        self.c = Canvas(root, height=250, width=250, bg='white')
        self.c.pack(fill=BOTH, expand=True)

        frame1 = Frame(self.c)
        frame1.pack(side='top')

        self.c.bind('<Configure>', self.createGrid)
        self.pixel_width = 20
        self.pixel_height = 20

        # Setup binds
        self.c.bind("<ButtonPress-1>", self.leftClick)

        self.menu = Canvas(root, height = 250, width = 250, bg='white')
        self.menu.pack()
        self.c.pack(fill=BOTH, expand=True)
        self.new_game_button = Button(root, text = "New Game", command = self.new_game)
        self.new_game_button.pack()

        frame2 = Frame(self.menu)
        frame2.pack(side='bottom')

    def leftClick(self, event):
        items = self.c.find_closest(event.x, event.y)
        if items:
            rect_id = items[0]
            self.c.itemconfigure(rect_id, fill="red")
            print(rect_id)

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
        mine_amount = int(input("Mine Amount: "))
        mine_coords = []
        for i in range(mine_amount):
            self.mine_placement()
            mine_coords.append(self.mine_coord)
        print(mine_coords)
        self.number_generation(mine_coords)


    def mine_generation(self):
        x_coord = random.randint(0, 9)
        y_coord = random.randint(0, 9)
        coord_process = str(x_coord) + str(y_coord)
        final_coord = int(coord_process)
        if final_coord == 10:
            x_coord = random.randint(0, 9)
            y_coord = random.randint(1, 9)
            coord_process = str(x_coord) + str(y_coord)
            final_coord = int(coord_process)
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
        for x in range(0, 10):
            for y in range(1, 11):
                x_coord = x
                y_coord = y
                coord = str(x_coord) + str(y_coord)
                coord = int(coord)
                if coord not in mine_coords:
                    mines_prox = self.proximity_check(coord, mine_coords)
                    if mines_prox == 0:
                        print("run the big boy function")
                    if mines_prox == 1:
                        self.c.itemconfigure(coord, fill="light grey")
                    if mines_prox == 2:
                        self.c.itemconfigure(coord, fill="gray")
                    if mines_prox == 3:
                        self.c.itemconfigure(coord, fill="green")
                    if mines_prox == 4:
                        self.c.itemconfigure(coord, fill="orange")
                    if mines_prox == 5:
                        self.c.itemconfigure(coord, fill="red")
                    if mines_prox == 6:
                        self.c.itemconfigure(coord, fill="pink")
                    if mines_prox == 7:
                        self.c.itemconfigure(coord, fill="purple")
                    if mines_prox == 8:
                        self.c.itemconfigure(coord, fill="black")


    
    def proximity_check(self, coord, mine_coords):
        nums = self.coord_splitter(coord)
        x_coord = nums[0]
        y_coord = nums[1]
        total_mines_in_prox = 0

        if y_coord == "0" or y_coord == "00":
            y_coord = 1
        
        if x_coord == "0" or x_coord == "00":
            x_coord = 1
    

        print(mine_coords)

        #Function is very long, could possibly take code after coord 
        #processing and put into a method or possibly a class

        print("-y x Func")
        new_y_coord = int(y_coord) - 1
        if int(y_coord) <= 0:
            updated_coord = str(new_y_coord)
        else:
            updated_coord = str(x_coord) + str(new_y_coord)
        print(updated_coord)
        updated_coord = int(updated_coord)
        print("Updated Coord:", updated_coord)
        for mine_coord in mine_coords:
            if mine_coord == updated_coord:
                total_mines_in_prox += 1
                break

        print(total_mines_in_prox)

        print("-y -x Func")

        new_y_coord = int(y_coord) - 1
        new_x_coord = int(x_coord) - 1
        updated_coord = str(new_x_coord) + str(new_y_coord)
        updated_coord = int(updated_coord)
        print("Updated Coord:", updated_coord)
        for mine_coord in mine_coords:
            if mine_coord == updated_coord:
                total_mines_in_prox += 1
                break

        print(total_mines_in_prox)

        print("y -x Func")
        new_x_coord = int(x_coord) - 1
        updated_coord = str(new_x_coord) + str(y_coord)
        updated_coord = int(updated_coord)
        print("Updated Coord:", updated_coord)
        for mine_coord in mine_coords:
            if mine_coord == updated_coord:
                total_mines_in_prox += 1
                break

        print(total_mines_in_prox)

        print("+y -x Func")
        new_y_coord = int(y_coord) + 1
        new_x_coord = int(x_coord) - 1
        updated_coord = str(new_x_coord) + str(new_y_coord)
        updated_coord = int(updated_coord)
        print("Updated Coord:", updated_coord)
        for mine_coord in mine_coords:
            if mine_coord == updated_coord:
                total_mines_in_prox += 1
                break

        print(total_mines_in_prox)

        print("+y x Func")
        new_y_coord = int(y_coord) + 1
        updated_coord = str(x_coord) + str(new_y_coord)
        updated_coord = int(updated_coord)
        print("Updated Coord:", updated_coord)
        for mine_coord in mine_coords:
            if mine_coord == updated_coord:
                total_mines_in_prox += 1
                break

        print(total_mines_in_prox)

        print("+y +x Func")
        new_y_coord = int(y_coord) + 1
        new_x_coord = int(x_coord) + 1
        updated_coord = str(new_x_coord) + str(new_y_coord)
        updated_coord = int(updated_coord)
        print("Updated Coord:", updated_coord)
        for mine_coord in mine_coords:
            if mine_coord == updated_coord:
                total_mines_in_prox += 1
                break
        
        print(total_mines_in_prox)

        print("y +x Func")
        new_x_coord = int(x_coord) + 1
        updated_coord = str(new_x_coord) + str(y_coord)
        updated_coord = int(updated_coord)
        print("Updated Coord:", updated_coord)
        for mine_coord in mine_coords:
            if mine_coord == updated_coord:
                total_mines_in_prox += 1
                break

        print(total_mines_in_prox)

        print("-y +x")
        new_y_coord = int(y_coord) - 1
        new_x_coord = int(x_coord) + 1
        if new_y_coord <= 0:
            updated_coord = str(new_x_coord)
        else:
            updated_coord = str(new_x_coord) + str(new_y_coord)
        updated_coord = int(updated_coord)
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