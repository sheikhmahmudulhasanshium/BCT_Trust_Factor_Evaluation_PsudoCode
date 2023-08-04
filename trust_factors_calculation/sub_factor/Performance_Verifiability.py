
def score_pv(para):
  PV = 0
  for sentence in para:
    if sentence says BCT system can verify the performance most of the part  and fail to judge some parts, which problem is unsolved yet and has clear evidence that risk causing loss that means this performance verifiability of the system is very low:
      PV = 1
    elif sentence says BCT system can verify the performance most of the part and fail to judge some parts, which problem is unsolved yet:
      PV = 3
    elif sentence says If the BCT is somewhat better than other technologies, it should have a defined standard method that verifies the claim of performance, and the superiority claim is technically legit, and it has some ignorable limitations:
      PV = 5
    elif sentence says BCT is superior to other technology it should have a defined standard method that verifies the claim of performance and if the superiority claim are legit and it has some ignorable limitations:
      PV = 7
    elif sentence says BCT is superior to other technology it should have a defined standard method that verifies the claim of performance, and the superiority claim is legit:
      PV = 9
  return PV

for para in document:
  PV = score_pv(para)


