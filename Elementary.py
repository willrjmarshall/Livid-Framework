import Live
from LividConstants import *

from RGBButtonElement import RGBButtonElement
from _Framework.EncoderElement import EncoderElement
from _Framework.ButtonElement import ButtonElement

class Elementary(object):
  """ This mixin provides shared methods to allow modular control of the encoder and button classes """
  
  # We default to these classes
  # BUT any class using Elementary as a mixin can have these overriden on __init__
  def __init__(self, button_class = RGBButtonElement, encoder_class = EncoderElement):
    # We allow the initializer of this class to manually set which Element abstractions to use!
    self.encoder_class = encoder_class
    self.button_class = button_class

  def encoder(self, cc):
    """ Build an encoder using parameters stored in the class"""
    return self.encoder_class(MIDI_CC_TYPE, self.channel, cc, Live.MidiMap.MapMode.absolute)

  def button(self, note, **kwargs):
    return self.button_class(True, MIDI_NOTE_TYPE, self.channel, note, **kwargs)
