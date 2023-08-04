def calculate_factors():
  TA = round((TS + TV) / 2)
  FA = -TA
  CA = round((RE + SE) / 2)
  MC = -CA
  BI = round((PE + EE + SI) / 3)
  PU = round((Im + PV + JR + Ex + SI) / 5)
  IB = round((FA + MC + SC + BI + PU) / 5)
  TL = IB * 10
  return TA, FA, CA, MC, BI, PU, IB, TL

def main():
  TA, FA, CA, MC, BI, PU, IB, TL = calculate_factors()
 
if __name__ == "__main__":
  main()
