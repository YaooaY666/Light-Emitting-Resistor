"""
    (A̅+B̅)(C̅+B̅)(A+B̅+C)(B)+AC̅+ABC+(B̅+C)(A̅+B+C̅)(A)
=   AC̅ + AB

"""

class TruthValue:
    def __init__(self, truth):
        self.truth = truth
    
    def __add__(self, other):
        value = self.truth + other.truth
        if value != 0:
            value = 1
        return TruthValue(value)
    
    def __mul__(self, other):
        value = self.truth * other.truth
        return TruthValue(value)
    
    def __invert__(self):
        return TruthValue(1 - self.truth)
    
def print_truth(truth):
    if truth == 0:
        return False
    return True

def truth_table(num): 
    A = TruthValue(num & 1)
    B = TruthValue((num >> 1) & 1)
    C = TruthValue((num >> 2) & 1)
    Og_Exp = ((~A + ~B)*(~C+ ~B)*(A + ~B + C)*B + A*(~C) + A*B*C +(~B + C)*(~A + B + ~C)*A)
    Sim_Exp = (A*(~C) + A*B)
    print(print_truth(A.truth), "\t", 
          print_truth(B.truth), "\t", 
          print_truth(C.truth), "\t", 
          print_truth(Og_Exp.truth), "\t",
          print_truth(Sim_Exp.truth))


print("A\tB\tC\tOg_Exp\tSim_Exp")
for num in range(0, 8):
    truth_table(num)

"""for num in range(0, 8):
    print(num & 1, "\t", (num >> 1) & 1, "\t", (num >> 2) & 1)"""

