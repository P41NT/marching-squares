from tkinter import *
from random import *
from opensimplex import OpenSimplex
import math
import time

def main():

    screen = Tk()
    screen.geometry("1000x1000")

    canvas = Canvas(screen, bg="black", width=1000, height=1000)

    simplex = OpenSimplex()

    def scale(x):
        return 1 if x > 0 else 0

    def line(a, b):
        canvas.create_line(a[0], a[1], b[0], b[1], fill='white')

    resolution = 20 
    z_off = 0
    columns = rows = 1 + 1000 // resolution

    while True:

        z_off = z_off + 1
        area = [[scale(simplex.noise3d(x=j * resolution, y=i * resolution, z=z_off))*255 for j in range(columns)] for i in range(rows)]

        # for i in range(columns):
        #     for j in range(rows):
        #         color = area[i][j]
        #         canvas.create_oval(i*resolution-0.3, j*resolution-0.3, i*resolution+0.3, j*resolution+0.3, width = 0, fill = _from_rgb((color,color,color)))

        for i in range(columns - 1):
            for j in range(rows - 1):
                color = area[i][j]
                x = i * resolution
                y = j * resolution
                a = (x + resolution * 0.5, y)
                b = (x + resolution, y + resolution * 0.5)
                c = (x + resolution * 0.5, y + resolution)
                d = (x, y + resolution * 0.5)

                state = [area[i][j]//255, area[i+1][j]//255, area[i+1][j+1]//255, area[i][j+1]//255]
                
                if state == [0,0,0,1]:
                    line(c, d)
                elif state == [0,0,1,0]:
                    line(b, c)
                elif state == [0,0,1,1]:
                    line(b, d)
                elif state == [0,1,0,0]:
                    line(a, b)
                elif state == [0,1,0,1]:
                    line(a, d)
                    line(b, c)
                elif state == [0,1,1,0]:
                    line(a, c)
                elif state == [0,1,1,1]:
                    line(a, d)
                elif state == [1,0,0,0]:
                    line(a, d)
                elif state == [1,0,0,1]:
                    line(a, c)
                elif state == [1,0,1,0]:
                    line(a, b)
                    line(c, d)
                elif state == [1,0,1,1]:
                    line(a, b)
                elif state == [1,1,0,0]:
                    line(b, d)
                elif state == [1,1,0,1]:
                    line(b, c)
                elif state == [1,1,1,0]:
                    line(d, c)

        canvas.pack()
        time.sleep(2)    

        screen.update()
        canvas.delete("all")
main()
