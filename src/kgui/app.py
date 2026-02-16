from pygame.display import set_mode, update, set_caption, set_icon
from pygame.display import init as dislpay_init
from pygame.time import Clock
from pygame.event import get as get_events
from pygame import QUIT, quit, init


from kgui.screen import Screen
from kgui.visuals import Image

from sys import exit as system_exit

import asyncio

def check_quit(event_list):
    for event in event_list:
            if event.type==QUIT: 
                quit()
                system_exit()
                break 

class App:
    width, height = size = (500, 500)
    framerate: int = 60
    active_screen = Screen
    caption: str = "KUI App"
    logo: str = f'{"/".join(__file__.split('/')[:-1])}/assets/default-logo.png'
    def __init__(self, *args, **kwds):
        match args, kwds:
            case (), {}: pass
        
        self.clock = Clock()
        self.window = set_mode(self.size)
        dislpay_init()
        self.active_screen = self.active_screen(self.window)

        set_caption(self.caption)
        set_icon(Image(self.logo).surface)


    def update(self, dt, event_list): pass
    def run(self) -> None:
        init()
        running       = True
        window        = set_mode(self.size)
        dislpay_init()
        self.active_screen = self.active_screen(window)
        active_screen = self.active_screen
        clock         = Clock()
        frame         = 0
        while running:
            dt = clock.tick(self.framerate) / 1000 #time elapsed in seconds
            event_list = get_events()
            self.check_quit(event_list)
            self.update(dt, event_list)
            active_screen.update(dt, event_list)
            window.blit(active_screen, (0, 0))
            update()
            frame += 1
import time
async def asleep(dt): time.sleep(dt)

class AsyncApp(App):
    def __init__(self, *args, **kwds):
        self.async_tasks = [a() for a in args if asyncio.iscoroutinefunction(a)]
        other_args = [a for a in args if a not in self.async_tasks]
        App.__init__(self, *other_args, **kwds)
        self.frame = 0

    async def update_display(self):
        while self.running:
            dt = self.clock.tick(self.framerate) / 1000
            event_list = get_events()
            check_quit(event_list)
            self.active_screen.update(dt, event_list)
            self.window.blit(self.active_screen, (0, 0))
            update() #updates the display
            self.frame += 1
            if self.verbose: print("="*30, f"FRAME {self.frame}","="*30)
            await asyncio.sleep(0)

    async def main(self):
        await asyncio.gather(self.update_display(), *self.async_tasks)

    def run(self):
        self.running = True 
        loop = asyncio.get_event_loop()
        loop.create_task(self.update_display())
        for a in self.async_tasks: loop.create_task(a)
        asyncio.set_event_loop(loop)
        loop.run_forever()
