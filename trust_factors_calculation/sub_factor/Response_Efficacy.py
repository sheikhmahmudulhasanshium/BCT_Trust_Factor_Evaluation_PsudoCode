def score_re(para):
  RE = 0
  for sentence in para:
    if sentence says BCT has unsolved problem that reduces trust in protective measures enough to switch to other technology:
      RE = 1
    elif sentence says BCT system is unable to give solution to the problem which, if it occurs by taking own protection of the system, may not work against the risk:
      RE = 3
    elif sentence says BCT has available protective measure that is not mature enough, by using BCT a user may not be able to overcome all kinds of risks:
      RE = 5
    elif sentence says BCT has some problem which is ignorable, but the risks can be avoided by using established and standard protective measures:
      RE = 7
    elif sentence says BCT has no threat that means the system is successful in keeping it immutable to threat by taking its built-in protective measure:
      RE = 9
  return RE

for para in document:
  RE = score_re(para)
