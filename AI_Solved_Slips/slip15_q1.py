class MonkeyBananaProblem:
    def __init__(self):
        self.box_position = "initial"
        self.monkey_position = "floor"
        self.banana_position = "ceiling"
        self.has_box = False

    def move_box_to_wall(self):
        if self.box_position == "initial":
            print("Moving box to the wall...")
            self.box_position = "wall"
        else:
            print("The box is already at the wall.")

    def climb_on_box(self):
        if self.box_position == "wall" and self.monkey_position == "floor" and not self.has_box:
            print("Climbing on the box...")
            self.monkey_position = "box"
            self.has_box = True
        else:
            print("Cannot climb on the box. Make sure the box is at the wall and the monkey is on the floor.")

    def reach_banana(self):
        if self.monkey_position == "box" and self.banana_position == "ceiling":
            print("Reaching for the banana...")
            self.banana_position = "reached"
        else:
            print("Cannot reach the banana. Make sure the monkey is on the box and the banana is still on the ceiling.")

    def climb_down(self):
        if self.monkey_position == "box" and self.has_box:
            print("Climbing down from the box...")
            self.monkey_position = "floor"
            self.has_box = False
        else:
            print("Cannot climb down. Make sure the monkey is on the box.")

    def solve(self):
        self.move_box_to_wall()
        self.climb_on_box()
        self.reach_banana()
        self.climb_down()
        print("Problem solved!")


# Create an instance of the MonkeyBananaProblem class and solve the problem
monkey_problem = MonkeyBananaProblem()
monkey_problem.solve()
