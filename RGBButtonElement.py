from _Framework.ButtonElement import ButtonElement
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
      on_color = GREEN,
      off_color = RED): 
    ButtonElement.__init__(self, is_momentary, msg_type, channel, identifier)
    
    self.on_color = int(on_color)
    self.off_color = int(off_color)

  def turn_on(self):
    self.send_value(self.on_color)

  def turn_off(self):
    self.send_value(self.off_color)
