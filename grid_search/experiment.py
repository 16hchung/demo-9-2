from pathlib import Path
import fire

from util import constants as C

class Experiment:

  def __init__(self, arg1=C.DEFAULT_ARG1,
                     arg2=C.DEFAULT_ARG2,
                     output_rt='test'):
    print('load data / other setup before running experiment, which will'
         f'save to {output_rt}')
    self.arg1 = arg1
    self.arg2 = arg2
    paths = self.make_paths(output_rt)
    self.confusion_path, self.score_path, self.confusion_fig_path = paths

  def run(self):
    print('running!')

  @staticmethod
  def make_paths(output_rt):
    output_rt = Path(output_rt)
    output_rt.mkdir(exist_ok=False, parents=True)
    confusion_matrix = output_rt / 'confusion_matrix.csv'
    score_report = output_rt / 'score_report.txt'
    figures = output_rt / 'figures'
    figures.mkdir(exist_ok=True, parents=True)
    pretty_confusion_matrix = figures / 'confusion_matrix.png'
    return confusion_matrix, score_report, pretty_confusion_matrix

def try_experiment(arg1, arg2, name):
  output_rt = C.DATA_RT / name
  experiment = Experiment(arg1, arg2, output_rt)
  experiment.run()

if __name__=='__main__':
  fire.Fire()
