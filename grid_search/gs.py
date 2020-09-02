import numpy as np
import pickle as pk

from .experiment import Experiment
from util.util import generate_arg_combos, stringify_args
from util import constants as C

class GridSearch:

  def __init__(self, arg1_options=[0,1], arg2_options=[2,3]):
    self.arg1_options = arg1_options
    self.arg2_options = arg2_options
    # load data that's shared among all options

  @classmethod
  def from_file(cls, fpath):
    with open(fpath, 'rb') as f:
      hparams = pk.load(f)
    arg1_options, arg2_options = hparams
    return cls(arg1_options=arg1_options, arg2_options=arg2_options)

  def save(self, fpath):
    with open(fpath, 'wb') as f:
      pk.dump([self.arg2_options, self.arg2_options], f)

  def run(self, output_path=C.DATA_RT):
    # TODO DEMO DEBUGGER HERE
    experiment_options = generate_arg_combos(arg1=self.arg1_options,
                                             arg2=self.arg2_options)
    for options in experiment_options:
      exp_name = stringify_args(**options)
      experiment = Experiment(**options, output_rt=output_path / exp_name)
      experiment.run()

if __name__=='__main__':
  gs = GridSearch()
  gs.run()
