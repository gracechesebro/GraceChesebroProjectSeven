import random
import dearpygui.dearpygui as dpg
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
child_w, child_h, channels, child_raw = dpg.load_image("girl1.png")
truck_w, truck_h, channels, truck_raw = dpg.load_image("truck_1_2.png")
dog_w, dog_h, channels, dog_raw = dpg.load_image("dog2.png")
bear_w, bear_h, channels, bear_raw = dpg.load_image("bear.png")
car_w, car_h, channels, car_raw = dpg.load_image("car2.png")
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
top_trucks = create_trucks(3)
dogs = [
    {"x": 200, "y": 350},
    {"x": 300, "y": 350}
]
bear = {"x": 400, "y": 350}

#textures
with dpg.texture_registry():
    dpg.add_static_texture(child_w, child_h, child_raw, tag="child_texture")
    dpg.add_static_texture(truck_w, truck_h, truck_raw, tag="truck_texture")
    dpg.add_static_texture(dog_w, dog_h, dog_raw, tag="dog_texture")
    dpg.add_static_texture(bear_w, bear_h, bear_raw, tag="bear_texture")
    dpg.add_static_texture(car_w, car_h, car_raw, tag="car_texture")
#handler
with dpg.handler_registry():
    dpg.add_key_press_handler(callback=move_child)

#window / drawlist
dpg.create_viewport(title="Project Seven Game", width = 800, height = 800)
with dpg.drawlist(width=800, height=800):
    #background
    dpg.draw_rectangle((0,0), (800,800), fill=comp151Colors.BLACK)
    #grocery store
    dpg.draw_rectangle((0,0), (800,120), thickness=4, color=comp151Colors.WHITE, fill=comp151Colors.BROWN)
    dpg.draw_text((20, 20), "GROCERY STORE", size=25)
    #grocery store doors
    #left door
    dpg.draw_rectangle((355, 25), (400, 115), thickness = 4, color=comp151Colors.WHITE,
                       fill=comp151Colors.GRAY)
    #right door
    dpg.draw_rectangle((400,25), (445, 115), thickness=4, color=comp151Colors.WHITE,
                       fill=comp151Colors.GRAY)
    #top road - don't have to draw - background is black already
    #Grass
    dpg.draw_rectangle((0,300), (800, 450), thickness=4, color=comp151Colors.WHITE,
                       fill=comp151Colors.DARK_GREEN)
    #Parking Lot
    x=50
    while x < 800:
        dpg.draw_line((x, 550), (x, 800), fill=comp151Colors.WHITE, thickness=4)
        x+=80


dpg.start_dearpygui
dpg.destroy_context


