import Live
from LividConstants import *
from _Framework.ControlSurface import ControlSurface
from RGBButtonElement import RGBButtonElement

class LividControlSurface(ControlSurface):
  """ Custom control surface with boilerplate handled """

  def __init__(self, c_instance):
    ControlSurface.__init__(self, c_instance)
    self.set_suppress_rebuild_requests(True) #Turn rebuild back on, now that we're done setting up
    self.awaiting_refresh = False
    self._device_selection_follows_track_selection = True
    self._suggested_input_port = ('Ohm')
    self._suggested_output_port = ('Ohm')
    self.setup_mixer()
    self.setup_session()
    self.setup_transport()
    self.setup_custom()
    self.log_message("Finished setting up")

  def refresh_state(self):
    ControlSurface.refresh_state(self)
    if not self.awaiting_refresh:
      self.awaiting_refresh = True
      self.schedule_message(1, self.refresh_on_timer)

  def refresh_on_timer(self):
    self.awaiting_refresh = False
    ControlSurface.refresh_state(self)
    self.set_suppress_rebuild_requests(False) #Turn rebuild back on, now that we're done setting up
    self.request_rebuild_midi_map()
    self.log_message("Refreshed state after 1 second delay")

  def request_rebuild_midi_map(self):
    self.log_message("Rebuilding MIDI map")
    ControlSurface.request_rebuild_midi_map(self)

  def setup_custom(self):
    pass

  def setup_mixer(self):
    raise AssertionError, 'Function setup_mixer must be overridden by subclass'

  def setup_session(self):
    raise assertionerror, 'function setup_session must be overridden by subclass'

  def setup_transport(self):
    raise assertionerror, 'function setup_transport must be overridden by subclass'

