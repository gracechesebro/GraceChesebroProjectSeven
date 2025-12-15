import random
import dearpygui.dearpygui as dpg
import comp151Colors
import SampleImages

#boiler plate
dpg.create_context()
WINDOW_W=800
WINDOW_H=800
#variables
#child starts at door
child_x = 370
child_y = 30
child_speed = 5
child_pet_dog = False
game_over = False
game_win = False
#speeds
truck_speed=3
dog_speed=2
bear_speed=2
dog_direction = 1
bear_direction = 1
#load images
child_w, child_h, channels, child_raw = dpg.load_image("SampleImages/girl1.png")
truck_w, truck_h, channels, truck_raw = dpg.load_image("SampleImages/truck_1_2.png")
truck2_w, truck2_h, channels, truck2_raw = dpg.load_image("SampleImages/garbage_1_2.png")
dog_w, dog_h, channels, dog_raw = dpg.load_image("SampleImages/dog2.png")
bear_w, bear_h, channels, bear_raw = dpg.load_image("SampleImages/bear.png")
car_w, car_h, channels, car_raw = dpg.load_image("SampleImages/car2.png")
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
def create_trucks(number, y_value):
    trucks = []
    for i in range(number):
        current_x = random.randint(0,700)
        current_truck = {
            "x": current_x,
            "y": y_value
        }
        trucks.append(current_truck)
    return trucks
def do_overlap(l1, r1, l2, r2):
    if l1.get("x") > r2.get("x") or l2.get("x") > r1.get("x"):
        return False
    if r1.get("y") < l2.get("y") or r2.get("y") < l1.get("y"):
        return False
    return True
#added more functions
def move_trucks(truck_list, speed):
    for t in truck_list:
        t["x"] += speed
        if t["x"] > 800:
            t["x"] = -truck_w
        elif t["x"] < -truck_w:
            t["x"] = 800

#checks for collisions with trucks, dogs, and bear
def check_collisions(px, py):
    global game_over, child_pet_dog
    #trucks
    for t in top_trucks:
        if do_overlap({"x": px, "y": py}, {"x":px+child_w, "y":py+child_h},
                      {"x": t["x"], "y": t["y"]}, {"x": t["x"] + truck_w, "y": t["y"] +
                                                                               truck_h}):
            game_over = True
    #dogs pet
    for d in dogs:
        if do_overlap({"x": px, "y": py}, {"x": px+ child_w, "y": py+child_h},
                      {"x": d["x"] + dog_w, "y": d["y"] + dog_h}):
            child_pet_dog = True
    #bear
    if do_overlap(l1={"x": px, "y": py}, r1={"x": px + child_w, "y": py + child_h},
                  l2={"x": bear["x"], "y": bear["y"]}, r2={"x": bear["x"] + bear_w,
                                                           "y": bear["y"] + bear_h}):
        game_over = True
#Creating Objects
top_trucks = create_trucks(3, 150)
bottom_trucks = create_trucks(3, 500)
dogs = [
    {"x": 200, "y": 350},
    {"x": 300, "y": 350}
]
bear = {"x": 400, "y": 350}

#textures
with dpg.texture_registry():
    dpg.add_static_texture(child_w, child_h, child_raw, tag="child_texture")
    dpg.add_static_texture(truck_w, truck_h, truck_raw, tag="truck_texture")
    dpg.add_static_texture(truck2_w, truck2_h, truck2_raw, tag="truck2_texture")
    dpg.add_static_texture(dog_w, dog_h, dog_raw, tag="dog_texture")
    dpg.add_static_texture(bear_w, bear_h, bear_raw, tag="bear_texture")
    dpg.add_static_texture(car_w, car_h, car_raw, tag="car_texture")
#handler
with dpg.handler_registry():
    dpg.add_key_press_handler(callback=move_child)

#window / drawlist
dpg.create_viewport(title="Project Seven Game", width = 800, height = 800)
with dpg.window(label="Project Seven Game Window", width=800, height=800):
    with dpg.drawlist(width=800, height=800):
    #background
        dpg.draw_rectangle((0,0), (800,800), fill=comp151Colors.BLACK)
    #grocery store
    dpg.draw_rectangle((0,0), (800,120), thickness=4, color=comp151Colors.WHITE,
                       fill=comp151Colors.SENNA)
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
    dpg.draw_text((200, 400), "", size=30, color=comp151Colors.WHITE, tag="status_text")
    #Parking Lot
    x=50
    while x < 800:
        dpg.draw_line((x, 550), (x, 800), color=comp151Colors.WHITE, thickness=4)
        x+=80
    #Images
    #car
    dpg.draw_image("car_texture", (350, 650), (350 + car_w, 650 + car_h),
                   tag="car_update")
    #child
    dpg.draw_image("child_texture", (child_x, child_y), (child_x + child_w,
                                                         child_y + child_h), tag="child_update")
    #top trucks
    count = 0
    for t in top_trucks:
        dpg.draw_image("truck_texture", (t["x"], t["y"]),
                       (t["x"] + truck_w, t["y"] + truck_h), tag=f"truck_update{count}")
        count += 1
    #bottom trucks
    count = 0
    for t in bottom_trucks:
        dpg.draw_image("truck2_texture", (t["x"], t["y"]), (t["x"] +
                                                            truck2_w, t["y"] + truck2_h),
                       tag=f"bottom_truck{count}")
        count += 1
    #dogs
    dpg.draw_image("dog_texture", (200, 350), (200+dog_w, 350+dog_h),
                   tag="dog_update")
    dpg.draw_image("dog_texture", (300, 350), (300+dog_w, 350+dog_h),
                   tag="dog2_update")
    #bear
    dpg.draw_image("bear_texture", (400, 350), (400+bear_w, 350+bear_h),
                   tag="bear_update")
#main loop
#loop runs continuously while the game is open, updates movement, checks collisions,
# and redraws objects.
dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    if not game_over:
        # move trucks
        i = 0
        for t in top_trucks:
            t["x"] -= 3
            if t["x"] < -truck_w:
                t["x"] = 800
            dpg.configure_item(f"truck_update{i}", pmin=(t["x"], t["y"]),
                               pmax=(t["x"] + truck_w, t["y"] + truck_h))
            #collision set up
            child_top_left = {"x": child_x, "y": child_y}
            child_bottom_right = {"x": child_x + child_w, "y": t["y"] + truck_h}
            truck_bottom_right = {"x": t["x"] + truck_w, "y": t["y"] + truck_h}
            #truck collision
            if do_overlap(child_top_left, child_bottom_right, t, truck_bottom_right):
                game_over = True
                dpg.configure_item("status_text", text="YOU LOST: CHILD HIT BY TRUCK - BAD PARENT")
                break
            i += 1
            #dog collision
            for d in dogs:
                dog_bottom_right = {"x": d["x"] + dog_w, "y": d["y"] + dog_h}
                if do_overlap(child_top_left, child_bottom_right, d, dog_bottom_right):
                    child_pet_dog = True
            #bear collision
            bear_bottom_right = {"x": bear["x"] + bear_w, "y": bear["y"] + bear_h}
            if do_overlap(child_top_left, child_bottom_right, bear, bear_bottom_right):
                game_over = True
                dpg.configure_item("status_text", text="YOU LOST: CHILD HIT BEAR - BAD PARENT")
            #car / win
            car = {"x": 350, "y": 650}
            car_bottom_right = {"x": 350 + car_w, "y": 650 + car_h}
            if child_pet_dog:
                game_win = True
                dpg.configure_item("status_text", text="YOU WIN: GOOD PARENT")
            else:
                dpg.configure_item("status_text", text="YOU LOST: CHILD CRIED - BAD PARENT")
    dpg.render_dearpygui_frame()

dpg.start_dearpygui
dpg.destroy_context


