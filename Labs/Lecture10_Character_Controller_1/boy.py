from pico2d import load_image

class Idle:
    @staticmethod
    def do():
        print("쿨쿨")
    @staticmethod
    def enter():
        print("고개 숙이기")
    @staticmethod
    def exit():
        print("눈뜨기")

    @staticmethod
    def draw():
        print("현호")

class StateMachine:
    def __init__(self):
        self.cur_state = Idle
        pass
    def start(self):
        self.cur_state.enter()
        pass
    def update(self):
        self.cur_state.do()
        pass
    def draw(self):
        self.cur_state.draw()
        pass

    pass


class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 0
        self.action = 3
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine()
        self.state_machine.start()

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.state_machine.update()

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.action * 100, 100, 100, self.x, self.y)
        self.state_machine.draw()