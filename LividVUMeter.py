import Live
from Elementary import Elementary
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent

class LividVUMeter(ControlSurfaceComponent, Elementary):
  """ An abstraction for a VU meter using a single MIDI CC"""

  def __init__(self, target, led_range = [0.52, 0.90], track = "master", **kwargs):
    ControlSurfaceComponent.__init__(self)
    Elementary.__init__(self, **kwargs)
    self.bottom = led_range[0] 
    self.top = led_range[1] 
    self.multiplier = (127 / (self.top - self.bottom))
    if target:
      self.setup_vu(target)

  def setup_vu(self, target):
    self.track = self.song().master_track
    self.target = self.encoder(target)
    self.prev_value = 0
    self.track.add_output_meter_left_listener(self.observe)

  def observe(self):
    int_value = self.level()
    if int_value is not self.prev_value:
      self.prev_value = int_value
      self.target.send_value(int_value, True)

  def level(self):
    return self.scale(self.track.output_meter_left)

  def scale(self, value):
    if (value > self.top):
      value = self.top
    elif (value < self.bottom):
      value = self.bottom
    value = value - self.bottom
    value = value * self.multiplier 
    value =  int(round(value))
    value = (value / 8) * 8 
    return value

  
  def update(self):
    return None
  
  def disconnect(self):
    self.track.remove_output_meter_left_listener(self.observe)
