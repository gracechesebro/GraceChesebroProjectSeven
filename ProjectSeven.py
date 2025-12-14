import random
import dearpygui as dpg
import comp151Colors
import SampleImages

#boiler plate
dpg.create_context()
#variables
child_x = 280
child_y = 320
child_speed = 6
child_pet_dog = False
game_over = False
game_win = False
#load images
child_w, child_h, c, child_raw = dpg.load_image("girl1.png")
truck_w, truck_h, c, truck_raw = dpg.load_image("truck_1_2.png")
dog_w, dog_h, c, dog_raw = dpg.load_image("dog2.png")
bear_w, bear_h, c, bear_raw = dpg.load_image("bear.png")
car_w, car_h, c, car_raw = dpg.load_image("car2.png")
#functions
#child
def move_child(sender, app_data):
    global child_x, child_y
    if game_over:
        return
    key = app_data
    if key == dpg.mvKey_Left:
        child_x -= child_speed
    elif key == dpg.mvKey_Right:
        child_x += child_speed
    elif key == dpg.mvKey_Up:
        child_y -= child_speed
    elif key == dpg.mvKey_Down:
        child_y += child_speed
    dpg.configure_item("child_update", pmin=(child_x, child_y), pmax=(child_x + child_w, child_y + child_h))
#function truck
def create_trucks(number):
    trucks = []
    for i in range(number):
        truck = {
            "x": random.randint(0,700),
            "y": 200
        }
        trucks.append(truck)
    return trucks
def do_overlap(l1, r1, l2, r2):
    if l1["x"] > r2["x"] or l2["x"] > r1["x"]:
        return False
    if r1["y"] < l2["y"] or r2["y"] < l1["y"]:
        return False
    return True
#Creating Objects

