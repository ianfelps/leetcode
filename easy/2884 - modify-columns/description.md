# 2884. Modify Columns
[LeetCode Link](https://leetcode.com/problems/modify-columns/description/)

```
DataFrame employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| salary      | int    |
+-------------+--------+
```

A company intends to give its employees a pay rise.

Write a solution to **modify** the `salary` column by multiplying each salary by 2.

The result format is in the following example.

# Comentários

Outro problema bem simples, utilizando pandas. Apenas pegamos os salários dos funcionarios, multiplicamos por 2 e retornamos os funcionarios atualizados.

```python
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.salary *= 2 # multiplica os salarios dos funcionarios por 2
    return employees # retorna os funcionarios com o salario modificado
```