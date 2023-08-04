def score_im(para):
  Im = 0
  for sentence in para:
    if sentence mentions that BCT technology has previously collapsed history and present evidence that means it has a huge risk:
      Im = 1
    elif sentence mentions that BCT technology has previously collapsed history that means it has some risk, but the risk is very unlikely to happen again:
      Im = 3
    elif sentence mentions that BCT has medium threat severity and threat vulnerability and some new and innovative concepts that make it better than other technologies and there are some solutions to problems that are immature:
      Im = 5
    elif sentence mentions that BCT has low threat severity and threat vulnerability and some new and innovative concepts and there are some ignorable problems:
      Im = 7
    elif sentence mentions that BCT has very low threat severity and threat vulnerability and some new and innovative concepts with no risk that other technologies face:
      Im = 9
  return Im

for para in document:
  Im = score_im(para)
