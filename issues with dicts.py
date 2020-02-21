import os
import site
import sys
import turtle

my_turtle = turtle.Turtle
turtle.speed(5)

# measurements in cm
# 10x for visibilty

# for drafting/universal
contants_dict = { 'north' : 90,
'south' : 270,
'west' : 180,
'east' : 0,
'cm' : 10,
'two_cm' : 20,
'an_inch' : 25,
'waistline' : 0,
}

# measurements from a person

your_sloper_dict = { 'nape_to_waist': 360,
'armhole_height' : 180,
'full_bust': 1000,
'waist_cir' : 740,
'bust_height' : 185,
'neck_cir' : 380,
'shoulder_len' : 120,
'front_width' : 670,
'back_width' : 510,
    }


# dart math

difference = (full_bust / 2) - (waist_cir / 2)
back_waist_dart = (difference / 3)
front_waist_dart = (back_waist_dart - cm)
side_waist_dart = (back_waist_dart + cm)


def horizontal_guide(guide_here, guide_len):
    # right side
    turtle.up()
    turtle.goto(-guide_len, guide_here)
    turtle.down()

    # left side
    turtle.goto(guide_len, guide_here)


def vertical_guide(guide_here, guide_len):
    turtle.up()
    #  guide, top
    turtle.goto(guide_here, guide_len)
    turtle.down()
    #  guide, bottom
    turtle.goto(guide_here, -guide_len)


def make_bodice_box(full_bust):
    box_len = (full_bust / 2)
    # top_right corner
    turtle.up()

    turtle.goto((-box_len), (your_sloper_dict.get('nape_to_waist') + contants_dict.get('cm'))
    back_line_top = turtle.pos()

    turtle.down()

"""
 # top_left corner

    turtle.goto(box_len, (nape_to_waist + cm))
    front_line_top = turtle.pos()

    turtle.up()
    # bottom_right corner
    turtle.goto((-box_len), waistline)
    turtle.down()
    waistline_front = turtle.pos()

    # bottom_left corner
    turtle.goto(box_len, waistline)
    waistline_back = turtle.pos()

    # top left to bottom left

    turtle.goto(waistline_back)
    turtle.goto(front_line_top)
    turtle.up()

    # top rt to bottom rt
    turtle.goto(back_line_top)
    turtle.down()
    turtle.goto(waistline_front)

    # neckline on backline
    turtle.goto(back_line_top)

    turtle.color("red")
    turtle.goto((-box_len), nape_to_waist)

    backline_neckline = turtle.pos()
    backline_x = turtle.xcor()

    # from backline, sq off 1/5 neck_cir on top
    turtle.up()
    turtle.goto(back_line_top)
    turtle.seth(east)
    turtle.down()
    turtle.forward(neck_cir / 5)
    back_shoulder_neckline = turtle.pos()

    # from back_shoulder_neckline, measure out 10cm to make the back_shoulder_slope
    turtle.up()
    turtle.forward(shoulder_len)
    turtle.seth(south)
    turtle.forward(cm)

    back_shoulder_slope_point = turtle.pos()
    back_shoulder_slope = turtle.heading()
    turtle.down()
    turtle.color("blue")

    # draw shoulder slope, line may need to be extended to match shoulder measurement

    turtle.goto(back_shoulder_neckline)

    # draw back neckline

    turtle.color("red")
    turtle.up()
    turtle.goto(backline_neckline)
    turtle.down()
    turtle.seth(east)
    this_far = (neck_cir / 6)
    turtle.forward(this_far)
    turtle.circle(20, 55)

    # mark out center_front_neckline
    turtle.up()
    turtle.goto(front_line_top)
    turtle.seth(south)

    turtle.down()
    turtle.forward((neck_cir / 5))

    # shoulder_front_neckline
    turtle.up()
    turtle.goto(front_line_top)
    turtle.seth(west)
    turtle.down()
    turtle.forward((neck_cir / 5))
    shoulder_front_neckline = turtle.pos()

    # draw in front neck line

    turtle.goto(shoulder_front_neckline)
    turtle.seth(south)
    turtle.circle((neck_cir / 5), 90)

    # front_shoulder_dart

    turtle.up()
    turtle.goto(shoulder_front_neckline)
    shoulder_dart = ((full_bust - front_width - back_width) / 3)
    turtle.color("yellow")
    turtle.seth(east)

    turtle.forward(shoulder_dart)
    outer_leg_shoulder_dart = turtle.pos()

    turtle.backward(shoulder_dart / 2)
    midpoint_shoulder_dart = turtle.pos()

    turtle.color("blue")

    turtle.up()
    turtle.goto(midpoint_shoulder_dart)
    turtle.seth(south)
    turtle.down()
    turtle.forward((nape_to_waist + cm))

    turtle.color("green")
    turtle.bk(bust_height)
    shoulder_dart_bustline = turtle.pos()
    turtle.color("orange")

    shoulder_dart_point = turtle.pos()

    turtle.goto(shoulder_front_neckline)
    turtle.up()
    turtle.goto(outer_leg_shoulder_dart)
    turtle.down()
    turtle.goto(shoulder_dart_point)

    turtle.forward(cm)
    front_dart_point = turtle.pos()
    front_dart_point_x = turtle.xcor()

    turtle.goto(front_dart_point_x, waistline)

    front_dart_midpoint = turtle.pos()

    # front shoulder

    turtle.up()
    turtle.goto(back_shoulder_slope_point)

    turtle.seth(south)
    turtle.forward(cm)
    # turtle.down()
    turtle.color("grey")

    # guide @ back shoulder - grey_line = guide from back shoulder to front shoulder
    grey_line_start = turtle.pos()
    grey_line_start_x = turtle.xcor()
    grey_line_start_y = turtle.ycor()

    # guide @ front shoulder
    front_shoulder_slope = turtle.heading()
    turtle.goto(outer_leg_shoulder_dart)
    grey_line_end = turtle.pos()
    grey_line_end_x = turtle.xcor()
    grey_line_end_y = turtle.ycor()

    turtle.seth(west)

    turtle.up()
    turtle.forward(shoulder_len)
    turtle.seth(south)
    turtle.forward(30)

    # blue line = front shoulder guide
    blue_line_pt = turtle.pos()
    blue_line_pt_x = turtle.xcor()
    blue_line_pt_y = turtle.ycor()

    front_shoulder_intersect = ((grey_line_end_y - grey_line_start_y) * (blue_line_pt_x - grey_line_start_x) / (
                grey_line_end_x - grey_line_start_x)) + (grey_line_start_y)

    round(front_shoulder_intersect)
    turtle.goto(blue_line_pt_x, front_shoulder_intersect)
    turtle.down()
    turtle.goto(outer_leg_shoulder_dart)
    turtle.color("green")

    # sq off front armhole @ shoulder
    turtle.up()
    turtle.goto(blue_line_pt_x, front_shoulder_intersect)
    turtle.down()
    turtle.forward(15)
    front_shoulder_sq_down = turtle.pos()

    # sq off back armhole @ shoulder
    turtle.up()
    turtle.goto(back_shoulder_slope_point)
    turtle.setheading(south)
    turtle.down()
    turtle.forward(15)
    back_shoulder_sq_down = turtle.pos()

    # on bustline, mark out 1/2 front_width + 1/2 dart
    turtle.up()
    turtle.goto(front_line_top)
    turtle.seth(west)
    turtle.forward(((front_width / 2) + (front_waist_dart / 2)))

    #   front_side_guide
    front_side_guide_x = turtle.xcor()
    front_side_guide_y = turtle.ycor()

    turtle.seth(south)
    turtle.down()
    turtle.forward((nape_to_waist + cm))

    # on bustline, mark out 1/2 back_width
    turtle.up()

    turtle.goto(back_line_top)
    turtle.seth(east)
    turtle.forward((back_width / 2))

    back_side_guide_x = turtle.xcor()
    back_side_guide_y = turtle.ycor()

    turtle.seth(south)
    turtle.down()
    turtle.forward((nape_to_waist + cm))

    # find and mark midpoint of front_side_guide and back_side_guide at bust_height- doesnt work as a function
    turtle.up()
    side_seam_guide = (((front_side_guide_x + back_side_guide_x) / 2), ((armhole_height + armhole_height) / 2))
    turtle.goto(side_seam_guide)

    side_dart_point = turtle.pos()

    turtle.seth(south)
    turtle.down()
    turtle.forward(armhole_height)
    side_dart_midpoint = turtle.pos()

    # divide back section in half, mark from bust_height to waistline
    turtle.up()
    turtle.goto(backline_x, bust_height)

    backline_y = turtle.ycor()

    back_dart_guide = (((back_side_guide_x + backline_x) / 2), ((backline_y + backline_y) / 2))
    turtle.goto(back_dart_guide)

    back_dart_point = turtle.pos()

    turtle.seth(south)
    turtle.down()
    turtle.forward(bust_height)
    back_dart_midpoint = turtle.pos()

    # back armhole_height/3 at back_side_guide_x
    turtle.up()
    # changed from bust height to armhole
    turtle.goto(back_side_guide_x, armhole_height)
    back_armhole_ref = turtle.pos()

    turtle.seth(north)
    turtle.down()
    turtle.color("red")
    # turtle.forward((armhole_height/3))
    turtle.forward((armhole_height / 4))
    back_armhole_notch = turtle.pos()

    # front armhole_height/4 front_side_guide_x
    turtle.up()

    # changed from bust height to armhole
    turtle.goto(front_side_guide_x, armhole_height)
    front_armhole_ref = turtle.pos()

    turtle.seth(north)
    turtle.down()
    # turtle.forward((armhole_height/4))
    turtle.forward((armhole_height / 5))
    front_armhole_notch = turtle.pos()

    # from back_armhole_ref draw a 2.5 cm diagonal line
    turtle.up()
    turtle.goto(back_armhole_ref)
    turtle.seth(((north + east) / 2))
    turtle.down()
    turtle.forward(an_inch)
    back_armpit_notch = turtle.pos()

    # front_armhole_ref draw a 2 cm diagonal line
    turtle.up()
    turtle.goto(front_armhole_ref)
    turtle.seth(((north + west) / 2))
    turtle.down()
    turtle.forward(two_cm)
    front_armpit_notch = turtle.pos()

    # connecting back armhole
    turtle.color("grey")
    turtle.up()
    turtle.goto(back_shoulder_sq_down)
    turtle.down()
    turtle.goto(back_armhole_notch)
    turtle.goto(back_armpit_notch)
    turtle.goto(side_dart_point)

    # connecting front armhole

    turtle.up()
    turtle.goto(front_shoulder_sq_down)
    turtle.down()
    turtle.goto(front_armhole_notch)
    turtle.goto(front_armpit_notch)
    turtle.goto(side_dart_point)

    # difference = (full_bust/2) - (waist_cir/2)

    # back_waist_dart = (difference/3)
    turtle.up()
    turtle.color("gold")

    turtle.goto(back_dart_midpoint)

    turtle.seth(west)
    turtle.forward(back_waist_dart / 2)
    turtle.down()
    turtle.goto(back_dart_point)
    turtle.goto(back_dart_midpoint)
    turtle.seth(east)

    turtle.forward(back_waist_dart / 2)
    turtle.goto(back_dart_point)

    # front_waist_dart = (back_waist_dart - cm)

    turtle.up()
    turtle.goto(front_dart_midpoint)

    turtle.seth(west)
    turtle.forward(front_waist_dart / 2)
    turtle.down()
    turtle.goto(front_dart_point)
    turtle.goto(front_dart_midpoint)
    turtle.seth(east)

    turtle.forward(front_waist_dart / 2)
    turtle.goto(front_dart_point)

    # side_waist_dart = (back_waist_dart + cm)

    turtle.up()

    turtle.goto(side_dart_midpoint)
    turtle.seth(west)

    turtle.forward(side_waist_dart / 2)
    turtle.down()
    turtle.goto(side_dart_point)
    turtle.goto(side_dart_midpoint)
    turtle.seth(east)

    turtle.forward(side_waist_dart / 2)
    turtle.goto(side_dart_point)


horizontal_guide(bust_height, (full_bust / 2))
make_bodice_box(full_bust)



"""
turtle.done()