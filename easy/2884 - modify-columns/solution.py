import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.salary *= 2 # multiplica os salarios dos funcionarios por 2
    return employees # retorna os funcionarios com o salario modificado