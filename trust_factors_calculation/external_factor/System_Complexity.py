def score_sc(para):
  SC = 0
  for sentence in para:
    if sentence mentions that BCT is very easy to understand for the user and the system is very easy to implement:
      SC = 1
    elif sentence mentions that BCT is relatively easy to understand because of reliable solutions and well-defined support, and the system is still difficult to maintain and implement when problems occur:
      SC = 3
    elif sentence mentions that BCT is sometimes difficult to understand because of its partially reliable solution and undefined support and is still difficult to maintain and implement when a problem occurs:
      SC = 5
    elif sentence mentions that BCT is most of the time difficult to understand because it has no existing solution and no reliable support and is very difficult to maintain and implement when a problem occurs:
      SC = 7
    elif sentence mentions that BCT has unsolved challenges of using BCT due to system complexity or the user is losing interest in using blockchain due to the high effort required to find and understand the solution of BCT:
      SC = 9
  return SC

for para in document:
  SC = score_sc(para)

