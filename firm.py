from sympy import *

class Firm:
    def __init__(self, fix_cost, marginal_cost, q):
        self.fix_cost = fix_cost
        self.marginal_cost = marginal_cost
        self.q = symbols(q)

    def cost(self):
        cost_func = self.fix_cost + self.marginal_cost * self.q
        return cost_func