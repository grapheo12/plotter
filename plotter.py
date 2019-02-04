"""Simple Graph Plotter.
    Call as: python plotter.py <filename.csv> <col_index_x> <col_index_y> <height> <width> <quadrant>
    Assumes first row contains row names.
    
    Copyright (C) 2019  Shubham Mishra

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import tkinter as tk
import sys
from math import floor

filename, col_x, col_y, height, width, quadrant = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]) 

root = tk.Tk()
graph = tk.Frame(root, height=height, width=width)
graph.pack()
canvas = tk.Canvas(graph, height=height, width=width, bg="white")
canvas.pack()

file = open(filename, "r")
lines = [i.split(",") for i in file.readlines()]
x_label = lines[0][col_x]
y_label = lines[0][col_y]

labels = tk.Label(root, text="x: " + x_label + "\ny: " + y_label)
labels.pack()

def point():
    global lines, col_x, col_y
    for i in lines[1:]:
        yield i[col_x], i[col_y]
     
p = point()
   
def plot():
    global canvas, p, height, width, quadrant
    try:
        i = 0
        while (i < 10):
            x, y = next(p)
            x, y = int(x), int(y)
            if quadrant == 1:
                canvas.create_oval(x, height - y, x+1, height - y - 1, fill="red")
            elif quadrant == 2:
                canvas.create_oval(x,floor(height/2) - y, x+1, floor(height/2) - y - 1, fill="red")
            elif quadrant == 4:
                canvas.create_oval(x+floor(width/2), floor(height/2) - y,x+1+floor(width/2),floor(height/2) - y - 1, fill="red")
            i += 1
        canvas.after(1, plot)
    except:
        print("Plot Complete")
        
if quadrant == 1:
    canvas.create_line( 0, 0, 0,  height - 1, fill="black")
    canvas.create_line( 0,  height - 1,  width - 1,  height - 1, fill="black")
elif quadrant == 2:
    canvas.create_line( 0,  0,  0,  height -1, fill="black")
    canvas.create_line( 0,  floor(height/2),  width -1,  floor(height/2), fill="black")
elif quadrant == 4:
    canvas.create_line( floor(width/2),  0, floor(width/2), height -1, fill="black")
    canvas.create_line( 0,  floor(height/2),  width -1,  floor(height/2), fill="black")
    
plot()
    
root.title("Plotter: "+filename)
tk.mainloop()

    
                    
            
        
    
    
    






