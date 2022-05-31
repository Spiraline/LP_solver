import argparse
from ortools.linear_solver import pywraplp
from os.path import exists

def LP_solver(objective, constraint, verbose):
    # Instantiate a GLOP solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Create the variables and let them take on any non-negative value.
    x = [solver.NumVar(0, solver.infinity(), 'x' + str(i)) for i in range(len(objective))]

    # Constraints
    for coeff in constraint:
        eq = 0
        for i, x_i in enumerate(x):
            if coeff[i] != 0:
                eq += coeff[i] * x_i
        if coeff[-2] == 'ge':
            solver.Add(eq >= coeff[-1])
        elif coeff[-2] == 'le':
            solver.Add(eq <= coeff[-1])
        else:
            solver.Add(eq == coeff[-1])

    if verbose:
        print('Number of variables =', solver.NumVariables())
        print('Number of constraints =', solver.NumConstraints())

    obj_eq = 0
    for i, x_i in enumerate(x):
        if objective[i] != 0:
            obj_eq += objective[i] * x_i

    solver.Maximize(obj_eq)

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        if verbose:
            print('[Solution]')
            print('Objective value =', solver.Objective().Value())
            for i, x_i in enumerate(x):
                print('x' + str(i), '=', x_i.solution_value())
    else:
        if verbose:
            print('The problem does not have an optimal solution.')
        return [], 'No optimal solution'

    if verbose:
        print('Problem solved in %f milliseconds' % solver.wall_time())
        print('Problem solved in %d iterations' % solver.iterations())

    return [x_i.solution_value() for x_i in x], solver.Objective().Value()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='LP Solver')
    parser.add_argument('--input', '-i', type=str, help='input file', required=True)
    parser.add_argument('--deli', '-d', type=str, help='delimiter', default=' ')
    parser.add_argument('--verbose', '-v', action='store_true', help='enable verbose')

    args = parser.parse_args()

    if not exists(args.input):
        print('Input file does not exist:', args.input)
        exit(1)

    const = []
    
    with open(args.input) as f:
        var_num, const_num = map(int, f.readline().rstrip().split(args.deli))

        obj = list(map(float, f.readline().rstrip().split(args.deli)))
        for _ in range(const_num):
            line = f.readline().rstrip().split(args.deli)
            for i in range(var_num+2):
                if i != var_num:
                    line[i] = float(line[i])
            
            const.append(line)

    optimal_var, optimal_obj = LP_solver(obj, const, args.verbose)
    print(optimal_var, optimal_obj)