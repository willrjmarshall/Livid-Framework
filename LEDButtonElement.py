from LividConstants import *
from Elementary import Elementary

from FlashingButtonElement import FlashingButtonElement
from _Framework.ButtonElement import ButtonElement

class LEDButtonElement(FlashingButtonElement):
  'Custom button element that can send state to multiple LEDs as needed'

  def __init__(self, 
      is_momentary,
      msg_type,
      channel,
      identifier,
      off_color = 0,
      on_color = 127,
      blink_on = False,
      blink_colors = [],
      color_mappings = None,
      **kwargs):

    FlashingButtonElement.__init__(self, is_momentary, msg_type, channel, identifier, 
        blink_on = blink_on, 
        blink_colors = blink_colors)
    
    self.setup_color_mappings(color_mappings)


  def setup_color_mappings(self, color_mappings):
    self.leds = {}
    if color_mappings is not None:
      for value, note_offset in color_mappings.items():
        adjusted_identifier = self._msg_identifier + note_offset
        self.leds[value] = ButtonElement(True, self._msg_type, self._msg_channel, adjusted_identifier)

  def send_value(self, value, force_send=False):
    if value == 0:
      FlashingButtonElement.send_value(self, value, force_send)
    else:
      if self.leds.has_key(value):
        self.leds[value].send_value(127, True)
      else:
        FlashingButtonElement.send_value(self, value, force_send)

