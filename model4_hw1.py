from pathlib import Path

def total_salary(path):
    try:  
        lines = []
        total_salary = 0
        average_salary = 0
        count = 0

        with open(path, "rt", encoding='utf-8') as fh:
            for el in fh.readlines():
                if el.find(",")>-1:
                    try:
                        total_salary +=float(el.strip().split(',').pop(1))
                    except ValueError as e:
                        print(e)
                        continue
                    count +=1
                else:
                    continue
                
            try:    
                average_salary = round(float(total_salary/count), 2)
            except ZeroDivisionError as e:
                print(e)

            lines.append(total_salary)
            lines.append(average_salary)
            lines = tuple(lines)
        return lines
    except OSError:
        print('Error while reading File') 
print(total_salary("text.txt"))
