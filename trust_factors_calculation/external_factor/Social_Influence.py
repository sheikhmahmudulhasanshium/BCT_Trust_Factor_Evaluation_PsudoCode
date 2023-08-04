for each para def score_si(para):
  SI = 0
  for sentence in para:
    if sentence mentions that BCT has strongly negative image and Social Influencer are leaving particular BCT for very high risk:
      SI = 1
    elif sentence mentions that BCT has negative image and Social Influencers are leaving particular BCT for high risk:
      SI = 3
    elif sentence mentions that BCT has average image and Social Influencers are neither encouraging nor leaving particular BCT for some risk:
      SI = 5
    elif sentence mentions that BCT has positive image and Social Influencers are encouraging particular BCT for very ignorable risk:
      SI = 7
    elif sentence mentions that BCT has very positive image and Social Influencers are strongly encouraging particular BCT for virtually no risk:
      SI = 9
  return SI

for para in document:
  SI = score_si(para)

