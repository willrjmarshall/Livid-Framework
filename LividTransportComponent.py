import Live
from LividConstants import *

from _Framework.TransportComponent import TransportComponent
from RGBButtonElement import RGBButtonElement

class LividTransportComponent(TransportComponent):
  def __init__(self, play = None, stop = None, channel = 0):
    TransportComponent.__init__(self)

    if play is not None:
      self.play_button = RGBButtonElement(True, MIDI_NOTE_TYPE, channel, play, off_color = PURPLE)
      self.set_play_button(self.play_button)
    if stop is not None:
      self.stop_button = RGBButtonElement(True, MIDI_NOTE_TYPE, channel, stop, on_color = RED, off_color = RED)
      self.set_stop_button(self.stop_button)

    

     
