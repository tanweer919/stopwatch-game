#"Stopwatch: The Game"
#Sit and enjoy
import simplegui
# define global variables
sec = 0
x = 0
y = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t // 600
    b = t % 600
    bc = b // 10
    d = t % 10
    if t % 600 < 100:
        st = str(a) + ":0" + str(bc) + "." + str(d)
    else:
        st = str(a) + ":" + str(bc) + "." + str(d) 
    return st
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global x, y, running
    if timer.is_running():
        y += 1
        if sec % 10 == 0:
            x += 1
    timer.stop()
    
    
def reset():
    global sec, x, y
    sec = 0
    x = 0
    y = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global sec
    sec += 1
    
# define draw handler
def draw(canvas):
    global x, y
    canvas.draw_text(format(sec),[100, 100], 40, "white")
    canvas.draw_text("%d/%d" %(x, y), [220, 30], 30, "Red")
    
# create frame
frame  = simplegui.create_frame("Stopwatch", 300, 200)
timer = simplegui.create_timer(100, tick)
# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 70)
frame.add_button("Stop", stop, 70)
frame.add_button("Reset", reset, 70)
# start frame
frame.start()


