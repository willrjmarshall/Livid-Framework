import Live

from LividConstants import *

from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ButtonElement import ButtonElement

class LividSessionComponent(SessionComponent):
  def __init__(self, matrix = [], channel = 0):
    # We can infer the width and height from the button matrix
    SessionComponent.__init__(self, len(matrix[0]), len(matrix))
    self.channel = channel 
    self.setup_matrix(matrix)
    # Scene launch buttons next

  def setup_matrix(self, matrix):
    self.button_matrix = ButtonMatrixElement() 

    for scene_index, row in enumerate(matrix):
      scene = self.scene(scene_index)
      scene.name = 'Scene_' + str(scene_index)
      button_row = [ButtonElement(True, MIDI_NOTE_TYPE, self.channel, cc) for cc in row]
      for i, cc in enumerate(row):
        clip_slot = scene.clip_slot(i) 
        clip_slot.set_triggered_to_play_value(YELLOW)
        clip_slot.set_triggered_to_record_value(PURPLE)
        clip_slot.set_stopped_value(RED)
        clip_slot.set_started_value(GREEN)
        clip_slot.set_launch_button(button_row[i])
      self.button_matrix.add_row(tuple(button_row))


