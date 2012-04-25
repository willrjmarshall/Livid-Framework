import Live

from LividConstants import *
from LividChanStripComponent import LividChanStripComponent
from RGBButtonElement import RGBButtonElement

from _Framework.MixerComponent import MixerComponent 
from _Framework.EncoderElement import EncoderElement 

class LividMixerComponent(MixerComponent):
  def __init__(self, 
    channel = 0, 
    sends = [], 
    mutes = [], 
    solos = [], 
    arms = [], 
    crossfader = None, 
    master = None, 
    cue = None, 
    button_class = RGBButtonElement, 
    encoder_class = EncoderElement, 
    faders = []):

    MixerComponent.__init__(self, len(faders))

    # Sanity checks
    # Use raise Exception NOT Assert
    if len(faders) is not len(mutes): 
      raise Exception("You must provide the same number of mute buttons as faders") 
    if len(faders) is not len(sends): 
      raise Exception("You must provide the same number of send encoder groups as faders") 

    # We allow the initializer of this class to manually set which Element abstractions to use!
    self.encoder_class = encoder_class
    self.button_class = button_class

    self.channel = channel
    self.num_tracks = len(faders)
    self.name = "Mixer"
    self.set_track_offset(0)

    # One for each channel
    self.build_channel_strips(mutes, faders, sends, solos, arms)

    # One-offs
    self.build_master(master)
    self.build_cue(cue)
    self.build_crossfader(crossfader)


  def build_channel_strips(self, mutes, faders, sends, solos, arms):
    """ Go through each channel strip, assign all the relevant controls"""
    mute_buttons = [self.button(note) for note in mutes]
    fader_encoders = [self.encoder(cc) for cc in faders] 
    solo_buttons = [self.button(note, on_color = PURPLE, off_color = BLUE) for note in solos]
    arm_buttons = [self.button(note, on_color = YELLOW, off_color = RED) for note in arms]

    for i in range(self.num_tracks): # We've previously asserted that we have matching lengths of mutes etc
      strip = self.channel_strip(i)
      strip.set_invert_mute_feedback(True)
      strip.set_volume_control(fader_encoders[i])
      strip.set_mute_button(mute_buttons[i])
      strip.set_arm_button(arm_buttons[i])
      strip.set_solo_button(solo_buttons[i])
      strip.set_send_controls(self.build_send_encoders(sends[i]))

  def build_master(self, master):
    """ Build and assign master volume fader if set """
    if master is not None:
      master_strip = self.master_strip()
      master_strip.set_volume_control(self.encoder(master))

  def build_cue(self, cue):
    """ Build and assign the cue volume control if set """
    if cue is not None:
      self.set_prehear_volume_control(self.encoder(cue))

  def build_crossfader(self, crossfader):
    if crossfader is not None:
      self.set_crossfader_control(self.encoder(crossfader))
    
  def build_send_encoders(self, cc_list):
    """ Build a tuple of encoders from a list of CCs"""
    return tuple([self.encoder(cc) for cc in cc_list])
  
  # Treat returns as tracks
  def tracks_to_use(self):
    return (self.song().visible_tracks + self.song().return_tracks)

  def encoder(self, cc):
    """ Build an encoder using parameters stored in the class"""
    return self.encoder_class(MIDI_CC_TYPE, self.channel, cc, Live.MidiMap.MapMode.absolute)

  def button(self, note, **kwargs):
    return self.button_class(True, MIDI_NOTE_TYPE, self.channel, note, **kwargs)


  def _create_strip(self):
    return LividChanStripComponent()
