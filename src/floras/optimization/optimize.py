from floras.optimization.setup_graphs import setup_nodes_and_edges
from floras.optimization.optimization import MILP

from ipdb import set_trace as st

def solve(virtual, system, b_pi, virtual_sys, case = 'static', print_solution=True, plot_results=False):
    GD, SD = setup_nodes_and_edges(virtual, virtual_sys, b_pi)

    milp = MILP(GD, SD, case)
    d, flow, exit_status = milp.optimize()
    if exit_status == 'opt':
        return d, flow
