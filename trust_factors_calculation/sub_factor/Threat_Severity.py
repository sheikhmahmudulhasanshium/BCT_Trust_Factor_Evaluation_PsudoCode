
def score_ts(para):
  TS = 0
  for sentence in para:
    if sentence does not have a problem that another technology has:
      TS = 1
    elif sentence has a problem that can be overlooked:
      TS = 3
    elif sentence has a solution to the problem but it is not matured or optimized enough:
      TS = 5
    elif sentence has evidence of an unsolved problem that is less likely to happen again:
      TS = 7
    elif sentence has evidence of an unsolved problem that reduced trust level significantly enough to switch to other technology:
      TS = 9
  return TS

for para in document:
  TS = score_ts(para)
