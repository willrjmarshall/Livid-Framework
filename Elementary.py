import Live
from LividConstants import *

from RGBButtonElement import RGBButtonElement
from _Framework.EncoderElement import EncoderElement
from _Framework.ButtonElement import ButtonElement

# NOTES
# In theory, we can strip this back and intercept the Button calls
# And we can force-map colors to greyscale as needed
# Also, flashing as needed

class Elementary(object):
  """ This mixin provides shared methods to allow modular control of the encoder and button classes, as well as some boilerplate """
  
  # We default to these classes
  # BUT any class using Elementary as a mixin can have these overriden on __init__
  def __init__(self, button_class = RGBButtonElement, encoder_class = EncoderElement, channel = 0):
    # We allow the initializer of this class to manually set which Element abstractions to use!
    self.channel = channel
    self.encoder_class = encoder_class
    self.button_class = button_class
    self.cached_callbacks = [] # Cache callbacks so we can tear them down on disconnect

  def encoder(self, cc):
    """ Build an encoder using parameters stored in the class"""
    return self.encoder_class(MIDI_CC_TYPE, self.channel, cc, Live.MidiMap.MapMode.absolute)

  def button(self, note, **kwargs):
    """ Create a button of the cached class, and attach event callbacks for blinking """
    if isinstance(note, dict):
      kwargs = dict(kwargs.items() + note.items())
      channel = note.get('channel', self.channel)
      button = self.button_class(True, MIDI_NOTE_TYPE, channel, kwargs.pop("note"), **kwargs)
    else:
      button =  self.button_class(True, MIDI_NOTE_TYPE, self.channel, note, **kwargs)

    if button.blink_on:
      self._register_timer_callback(button.blink)
      self.cached_callbacks.append(button.blink)
    return button

  def disconnect(self):
    for callback in self.cached_callbacks:
      self._unregister_timer_callback(callback)


