def score_jr(para):
  JR = 0
  for sentence in para:
    if sentence says BCT has no usefulness in the personal life of user or the alternative of BCT is so good that they do not need BCT:
      JR = 1
    elif sentence says BCT has some usefulness in the personal life of user which is very ignorable, or the alternative also has some:
      JR = 3
    elif sentence says BCT has some usefulness in the personal life of user and the user is not bound to use BCT to do his daily job:
      JR = 5
    elif sentence says BCT has very usefulness in personal life or without that BCT the user faces difficulty to do his daily job:
      JR = 7
    elif sentence says BCT has heavy usefulness in the personal life of user or without that particular BCT the user cannot do his daily job:
      JR = 9
  return JR

for para in document:
  JR = score_jr(para)

