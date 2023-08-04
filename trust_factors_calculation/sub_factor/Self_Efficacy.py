def score_se(para):
  SE = 0
  for sentence in para:
    if sentence says BCT user is conscious and careful while using BCT, but protective measure is not sufficient enough to avoid the risk:
      SE = 1
    elif sentence says BCT user is aware of the consequences of the risk and cannot take security measures of only BCT by himself, but if the user manages to find extraordinary and promising protection measures and stay careful enough, the loss of the risk might be mitigated:
      SE = 3
    elif sentence says BCT user is aware of the consequences of the risk and cannot take security measures of only BCT by himself, but if the risk appears, the user will be able to overcome the risk himself by using the BCT technology and self-awareness:
      SE = 5
    elif sentence says BCT has some problem, but if the mentioned risk appears, the user will be able to overcome the risk himself by using the BCT technology and self-awareness:
      SE = 7
    elif sentence says BCT has no threat, but if a risk happens by chance, the user will be able to overcome the risk himself by using the BCT technology and self-awareness:
      SE = 9
  return SE

for para in document:
  SE = score_se(para)

