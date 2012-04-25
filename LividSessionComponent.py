import Live

from LividConstants import *
from Elementary import Elementary

from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ButtonElement import ButtonElement
from RGBButtonElement import RGBButtonElement

# Fuck yeah multiple inheritance
class LividSessionComponent(SessionComponent, Elementary):
  def __init__(self, matrix = [], 
      navigation = None, 
      scene_launches = [], 
      stops = [], 
      mixer = False,
      **kwargs):

    # We can infer the width and height from the button matrix
    SessionComponent.__init__(self, len(matrix[0]), len(matrix))
    Elementary.__init__(self, **kwargs)


    self.setup_matrix(matrix)

    self.setup_stops(stops)

    if len(scene_launches) > 0:
      self.setup_scene_launch(scene_launches)

    self.setup_navigation(navigation)
    # Scene launch buttons next
   
    if mixer:
      self.set_mixer(mixer)

  def setup_stops(self, stops):
    self.set_stop_track_clip_buttons(tuple([self.button(note) for note in stops]))
    self.set_stop_track_clip_value(RED)

  def setup_scene_launch(self, scene_launches):
    self.scene_launch_buttons = [self.button(note, off_color = YELLOW) for note in scene_launches]
    
    for i, scene in enumerate(self._scenes):
      scene.set_launch_button(self.scene_launch_buttons[i])
      scene.set_triggered_value(PURPLE)

  def setup_navigation(self, navigation):
    if navigation is not None:
      self.up_button = self.button(navigation['up'], off_color = GREEN)    
      self.down_button = self.button(navigation['down'], off_color = GREEN)    
      self.left_button = self.button(navigation['left'], off_color = GREEN)    
      self.right_button = self.button(navigation['right'], off_color = GREEN)    
      self.set_scene_bank_buttons(self.down_button, self.up_button)
      self.set_track_bank_buttons(self.right_button, self.left_button)

  def setup_matrix(self, matrix):
    self.button_matrix = ButtonMatrixElement() 

    for scene_index, row in enumerate(matrix):
      scene = self.scene(scene_index)
      scene.name = 'Scene_' + str(scene_index)
      button_row = [self.button(cc, blink_on = True, off_color = OFF) for cc in row]
      for i, cc in enumerate(row):
        clip_slot = scene.clip_slot(i) 
        clip_slot.set_triggered_to_play_value(YELLOW)
        clip_slot.set_triggered_to_record_value(PURPLE)
        clip_slot.set_stopped_value(RED)
        clip_slot.set_started_value(GREEN)
        clip_slot.set_launch_button(button_row[i])
      self.button_matrix.add_row(tuple(button_row))


