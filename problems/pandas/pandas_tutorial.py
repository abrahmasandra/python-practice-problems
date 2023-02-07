import pandas as pd
import numpy as np

# TASK 1 Load the morg_d07_strings.csv data set into a "morg_df" variable here
# Note: The rest of the code in this file will not work until you've done this.

## YOUR CODE HERE ##
morg_df = pd.read_csv("data/morg_d07_strings.csv", index_col="h_id")

# TASKS 2-6
# For each of the tasks, print the value requested in the task.

## TASK 2
age = morg_df["age"]

## TASK 3
row = morg_df.loc["1_2_2", :]

## TASK 4
first_four = morg_df.iloc[:4, :]

## TASK 5
col_nan = {}
for col in morg_df.columns:
    if any(morg_df.loc[:, col].isna()):
        col_nan[col] = 0

## TASK 6
morg_df.fillna(col_nan, inplace=True)

### Task 7
### convert to categoricals
TO_CATEGORICALS = ["gender", "race", "ethnicity", "employment_status"]
for col in TO_CATEGORICALS:
    morg_df[col] = morg_df[col].astype("category")


# Example use of cut()
boundaries = range(16, 89, 8)
morg_df.loc[:, "age_bin"] = pd.cut(morg_df.loc[:, "age"],
                                   bins=boundaries,
                                   labels=range(len(boundaries)-1),
                                   include_lowest=True, right=False)

### Task 8

## YOUR CODE HERE ##
morg_df["hwpw_bin"] = 

print("Morg columns types after Task 8")
print(morg_df.dtypes)


### Tasks 9-13



### Task 14

students = pd.read_csv("data/students.csv")
extended_grades = pd.read_csv("data/extended_grades.csv")