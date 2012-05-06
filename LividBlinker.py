import Live
from RGBButtonElement import RGBButtonElement
from Elementary import Elementary
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent

class LividBlinker(ControlSurfaceComponent, Elementary):
  """ Control surface component that will init and blink an LED on a timer"""

  def __init__(self, led = None, **kwargs):
    ControlSurfaceComponent.__init__(self)
    Elementary.__init__(self, **kwargs)

    if led:
      self.setup_blinker(led)

  def setup_blinker(self, led):
    self.led = self.encoder(led)
    self.song().add_current_song_time_listener(self.blink)
    self.on = True
    self.counter = 0
    self.led.send_value(127)
    self._show_msg_callback("LOADED")
    self.prev_position = 0
    self.on = False

  def blink(self):
    position = int(self.song().current_song_time)
    if position > self.prev_position:
      self.prev_position = position
      if self.on: 
        self.on = False
        self.led.send_value(0, True)
      else:
        self.on = True
        self.led.send_value(127, True)

  def update(self):

    return None

  def disconnect(self):
    self.song().remove_current_song_time_listener(self.blink)
    return None

