from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90
sequence=1

while(True):
    if(sequence == 0):
        x=400
        y=90
        while(x<800):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x, y)
            x +=2
            delay(0.01)
        while(y<600):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x, y)
            y +=2
            x-=1.5
        while(y>90):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x, y)
            y -=2
            x-=1.5
        while(x<400):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x, y)
            x +=2
            delay(0.01)
        sequence=1;
    if (sequence == 1):
        r=210
        n=269
        while(n<270+4.3):
            clear_canvas_now()
            grass.draw_now(400,30)
            x=400 + r*math.cos(n)  
            y=300 + r*math.sin(n)
            character.draw_now(x, y)
            n+=0.1
            delay(0.1)
        sequence=0

    
 

close_canvas()
