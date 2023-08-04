def score_pe(para):
  PE = 0
  for sentence in para:
    if sentence says BCT has innovative features and versatility with unsolved problems and evidence of loss:
      PE = 1
    elif sentence says BCT has innovative features and versatility with unsolved problems:
      PE = 3
    elif sentence says BCT has innovative features and versatility with some problems having an immature solution:
      PE = 5
    elif sentence says BCT has innovative features and versatility with some ignorable problems:
      PE = 7
    elif sentence says BCT has innovative features and versatility with very low threat severity:
      PE = 9
  return PE

for para in document:
  PE = score_pe(para)


