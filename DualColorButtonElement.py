from _Framework.ButtonElement import ButtonElement
from LividConstants import *

class DualColorButtonElement(ButtonElement):
  'A modified ButtonElement that is Red when off and Green when on'

  def __init__(self, is_momentary, msg_type, channel, identifier): 
    ButtonElement.__init__(self, is_momentary, msg_type, channel, identifier)

  def turn_on(self):
    self.send_value(GREEN)

  def turn_off(self):
    self.send_value(RED)
