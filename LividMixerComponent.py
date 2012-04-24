import Live

from LividConstants import *

from _Framework.MixerComponent import MixerComponent 
from _Framework.EncoderElement import EncoderElement 

class LividMixerComponent(MixerComponent):
  def __init__(self, 
    num_tracks = 0, 
    num_returns = 0, 
    channel = 0, 
    faders = []):

    # Some basic sanity checking
    assert(len(faders) == num_tracks + num_returns)

    # Boilerplate
    MixerComponent.__init__(self, num_tracks, num_returns, False, False)
    
    # Here we set a lot of defaults that otherwise get copypasted
    self.name = "Mixer"
    self.set_track_offset(0)

    fader_encoders = [EncoderElement(MIDI_CC_TYPE, channel, cc,Live.MidiMap.MapMode.absolute) for cc in faders] 
    for i in range(num_tracks):
      strip = self.channel_strip(i)
      strip.set_volume_control(fader_encoders[i])
      #strip.set_mute_button(fader
