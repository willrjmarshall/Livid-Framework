from LividConstants import *
from RGBButtonElement import RGBButtonElement

from _Framework.SessionZoomingComponent import SessionZoomingComponent

class LividSessionZoomingComponent(SessionZoomingComponent):
  """ Customized session zoom component with a real init function """

  def __init__(self, session, shift, 
      unselected_color = RED,
      selected_color = GREEN,
      channel = 0):

    SessionZoomingComponent.__init__(self, session)
    
    # Get nav buttons, matrix, scene_launch buttons from session
    self.channel = channel

    self.set_button_matrix(session.button_matrix)
    self.set_zoom_button(RGBButtonElement(True, MIDI_NOTE_TYPE, self.channel, shift))

    self.set_stopped_value(unselected_color)
    self.set_selected_value(selected_color)

    self.set_nav_buttons(session.up_button, session.down_button, session.left_button, session.right_button)
    self.set_scene_bank_buttons(tuple(session.scene_launch_buttons))
