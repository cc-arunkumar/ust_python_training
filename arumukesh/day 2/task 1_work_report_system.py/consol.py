def consolidated_report(*args):
    n=len(args)
    sum=0
    for report in args:
        sum += report
    average = sum/n
    return average