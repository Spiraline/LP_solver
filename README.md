# LP Solver

LP Problem Solver with Google OR-Tools

## Usage

**[Requirement]**

- Python 3.6+
- PIP (upgrade recommended)

```
python -m pip install --upgrade pip
python -m pip install ortools argparse
```

**[Execution]**

```
git clone https://github.com/Spiraline/LP_solver.git
cd LP_solver
python lp_solver.py -i $(input file path)
```

**[Parmeter]**
- input (`-i`): input file path
- delimiter (`-d`): input file delimiter (default: ' ')
- verbose (`-v`): flags for log message

**[Input File Form]**
- Line 1: (variable #) (constraint #)
- Line 2: `max`/`min` and coefficient of objective function
- Line 3~: coefficient of constraint equation (Use `ge`, `le`, `eq` for operators)


## Example

<div style="text-align:center;">
    <img src="https://velog.velcdn.com/images/spiraline/post/1d3abef1-7bcf-4301-ab58-6031673d5be1/image.png" alt="example" width="300"/>
</div>

- Input File (same as `example` file)
```
2 3
max 3 4
1 -1 le 2
3 -1 ge 0
1 2 le 14
```

- Output
```
[5.999999999999998, 3.9999999999999996] 33.99999999999999
```
It means 3x+4y has maximum value 34 when x = 6 and y = 4.