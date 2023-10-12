from pico2d import *

hand = load_image('hand_arrow.png')
character = load_image('run_animation.png')
tuk_ground = load_image('TUK_GROUND.png')
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
running = True

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

open_canvas(TUK_WIDTH, TUK_HEIGHT)

# while running:
#     tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
#     character.clip_draw(0,0,100,102,TUK_WIDTH // 2, TUK_HEIGHT // 2)
#     update_canvas()
#     handle_events()

close_canvas()



