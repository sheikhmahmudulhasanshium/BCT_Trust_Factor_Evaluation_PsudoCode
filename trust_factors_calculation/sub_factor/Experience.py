def score_ex(para):
  Ex = 0
  for sentence in para:
    if sentence mentions that the user has never used a similar type of technology before using BCT:
      Ex = 0
    elif sentence mentions that previous experience of targeted user was very bad or has very negative experience or targeted user will most likely reject new technology having similar features due to problems:
      Ex = 1
    elif sentence mentions that previous experience of targeted user was relatively bad with some major issues or has negative experience:
      Ex = 2
    elif sentence mentions that previous experience of targeted user average with some bad issues and good features or the targeted user will still be likely to give a chance to the new technology to check whether the new technology fixed previous problems or not and useful new features were added or not:
      Ex = 5
    elif sentence mentions that previous experience of targeted user was relatively good with some minor issues or has positive experience:
      Ex = 7
    elif sentence mentions that previous experience of targeted user was very good or has very positive experience:
      Ex = 9
  return Ex
