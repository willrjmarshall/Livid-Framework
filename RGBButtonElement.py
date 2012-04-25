from _Framework.ButtonElement import ButtonElement
from _Framework.ControlSurface import ControlSurface
from LividConstants import *

MIDI_NOTE_TYPE = 0
MIDI_CC_TYPE = 1
MIDI_PB_TYPE = 2
MIDI_MSG_TYPES = (MIDI_NOTE_TYPE, MIDI_CC_TYPE, MIDI_PB_TYPE)
MIDI_NOTE_ON_STATUS = 144
MIDI_NOTE_OFF_STATUS = 128
MIDI_CC_STATUS = 176
MIDI_PB_STATUS = 224

class RGBButtonElement(ButtonElement):
  'Modified ButtonElement with configurable off and on states'

  def __init__(self, is_momentary, 
      msg_type, 
      channel, 
      identifier, 
      blink_on = False,
      on_color = GREEN,
      blink_colors = [YELLOW],
      off_color = RED): 

    ButtonElement.__init__(self, is_momentary, msg_type, channel, identifier)

    self.blink_on = blink_on
    self.blink_colors = set(blink_colors)
    self.blinking = False
    self.current_color = 0
    self.flash = True
    self.on_color = int(on_color)
    self.off_color = int(off_color)

  # Override to maintain state, then call super for actual changes
  def send_value(self, value):
    self.current_color = value
    if value > 0 and value is not self.off_color:
      self.blinking = True
    else:
      self.blinking = False
    super(RGBButtonElement, self).send_value(value)

  def turn_on(self):
    self.send_value(self.on_color)

  def turn_off(self):
    self.send_value(self.off_color)

  def blink(self):
    if self.blinking and self.current_color in self.blink_colors:
      if self._last_sent_value is not self.off_color and self._last_sent_value is not 0:
        super(RGBButtonElement, self).send_value(0)
      else:
        super(RGBButtonElement, self).send_value(self.current_color)
