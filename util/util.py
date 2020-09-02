import itertools

def generate_arg_combos(**kwargs):
  keys = kwargs.keys()
  vals = kwargs.values()
  for instance in itertools.product(*vals):
    yield dict(zip(keys, instance))

def stringify_args(**kwargs):
  arg_strs = []
  for k,v in kwargs.items():
    arg_strs.append(f'{k}-{v}')
  return '_'.join(arg_strs)
