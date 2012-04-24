import Live

from LividConstants import *

from _Framework.MixerComponent import MixerComponent 
from _Framework.EncoderElement import EncoderElement 

class LividMixerComponent(MixerComponent):
  def __init__(self, 
    channel = 0, 
    sends = [], 
    crossfader = None, 
    master = None, 
    cue = None, 
    faders = []):
    MixerComponent.__init__(self, len(faders))

    self.num_tracks = len(faders)
    
    # Here we set a lot of defaults that otherwise get copypasted
    self.name = "Mixer"
    self.set_track_offset(0)

    self.build_faders(channel, faders)
    self.build_sends(channel, sends)
    self.build_master(channel, master)
    self.build_cue(channel, cue)

    
    if crossfader is not None:
      self.set_crossfader_control(EncoderElement(MIDI_CC_TYPE, channel, crossfader, Live.MidiMap.MapMode.absolute))
  
  def build_cue(self, channel, cue):
    if cue is not None:
      self.set_prehear_volume_control(EncoderElement(MIDI_CC_TYPE, channel, cue, Live.MidiMap.MapMode.absolute))

  def build_master(self, channel, master):
    if master is not None:
      master_strip = self.master_strip()
      master_strip.set_volume_control(EncoderElement(MIDI_CC_TYPE, channel, master, Live.MidiMap.MapMode.absolute))

  def build_faders(self, channel, faders):
    """Build and assign faders as EncoderElements, from passed channel and list of fader CCs."""
    fader_encoders = [EncoderElement(MIDI_CC_TYPE, channel, cc, Live.MidiMap.MapMode.absolute) for cc in faders] 
    for i in range(self.num_tracks):
      strip = self.channel_strip(i)
      strip.set_volume_control(fader_encoders[i])

  def build_sends(self, channel, sends):
    """Build and assign send encoders, from channel and list of CCs"""
    for i in range(self.num_tracks):
      send_encoder_ccs = sends[i] # If not already a tuple, convert it.
      send_encoders = [EncoderElement(MIDI_CC_TYPE, channel, cc, Live.MidiMap.MapMode.absolute) for cc in send_encoder_ccs] 
      strip = self.channel_strip(i)
      strip.set_send_controls(tuple(send_encoders))
    

  # Treat returns as tracks
  def tracks_to_use(self):
    return (self.song().visible_tracks + self.song().return_tracks)
