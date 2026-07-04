with open("C:/Users/eklav/python learning/QSPR_dataset.csv","r") as f:
    for i, line in enumerate(f):
        print(line.strip())
        if i==4:
          bre