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

class FlashingButtonElement(ButtonElement):
  'Modified ButtonElement with a callback for blinking the "on" value'

  def __init__(self, is_momentary,
    msg_type,
    channel,
    identifier,
    blink_on = False,
    blink_colors = []):

    ButtonElement.__init__(self, is_momentary, msg_type, channel, identifier)

    self.blink_on = blink_on
    self.blink_colors = set(blink_colors)
    self.blinking = False
    self.current_color = 0

  # Override to maintain state, then call super for actual changes
  def send_value(self, value):
    self.current_color = value
    if value > 0 and value is not self.off_color:
      self.blinking = True
    else:
      self.blinking = False
    super(FlashingButtonElement, self).send_value(value)

  def blink(self):
    if self.blinking and self.current_color in self.blink_colors:
      if self._last_sent_value is not self.off_color and self._last_sent_value is not 0:
        super(FlashingButtonElement, self).send_value(0)
      else:
        super(FlashingButtonElement, self).send_value(self.current_color)
