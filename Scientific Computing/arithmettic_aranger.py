# %%
def arithmetic_arranger(problems, result = False):
    if len(problems)>5:
        return 'Error: Too many problems.'
    
    first = ''
    second = ''
    lines = ''
    sumx = ''

    for i in problems:
        li = i.split()
        op = li[1]
        fi = li[0]
        sc = li[2]

        if (fi.isdigit()==False or sc.isdigit()==False):
            return 'Error: Numbers must only contain digits.'

        if (len(fi)>4 or len(sc)>4):
            return 'Error: Numbers cannot be more than four digits.'

        if op == '+':
            final = str(int(fi)+int(sc))

        elif op == '-':
            final = str(int(fi)-int(sc))

        else:
            return "Error: Operator must be '+' or '-'."
        
        length = max(len(fi), len(sc))+2
        top = str(fi).rjust(length)
        bottom = op + str(sc).rjust(length - 1)
        line = ''
        res = str(final).rjust(length)
        for a in range(length):
            line += '-'

        if i != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            first += top
            second += bottom
            lines += line
            sumx += res

        if result:
            arranged_problems = '{}\n{}\n{}\n{}'.format(first, second, lines, sumx)
        else:
            arranged_problems = '{}\n{}\n{}'.format(first, second, lines)

    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
# %%
