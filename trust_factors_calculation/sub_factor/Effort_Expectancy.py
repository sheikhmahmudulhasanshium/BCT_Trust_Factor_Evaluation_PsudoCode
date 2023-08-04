
def score_ee(para):
  EE = 0
  for sentence in para:
    if sentence says BCT is superior to the other technology handling risk and BCT is very easy to understand, and the user do not have to go through more steps since no risk occurs:
      EE = 1
    elif sentence says BCT is superior to the other technology handling risk and the user might have to go through more well-defined steps if somehow any risk occurs:
      EE = 3
    elif sentence says BCT is superior to the other technology handling risk and the user might have to go through more unclear steps and be extra cautious if somehow any risk occurs:
      EE = 5
    elif sentence says BCT has past evidence of loss and the BCT user has to go through more steps most of the times and be extra cautious if somehow any risk occurs:
      EE = 7
    elif sentence says BCT has recent evidence of loss and the BCT user must go through more steps, be extra cautious all the time, and even use their own protective measures and experience if any risk occurs:
      EE = 9
  return EE

for para in document:
  EE = score_ee(para)
