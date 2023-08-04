
def scale(factor_name, score):
  """
  Scales the score of a factor to a value between 0 and 10.

  Args:
    factor_name: The name of the factor.
    score: The score of the factor.

  Returns:
    The scaled score.
  """

  if score >= 0:
    if score > 0 and score < 2:
      return score / 2
    elif score <= 2 and score < 4:
      return score / 3
    elif score <= 4 and score < 6:
      return score / 4
    elif score <= 6 and score < 8:
      return score / 5
    elif score <= 8 and score < 10:
      return score / 6
    else:
      return score / 7
  else:
    return (10 + score) / 11
