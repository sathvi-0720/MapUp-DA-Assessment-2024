from typing import List

def reverse_by_n_elements(lst: List[int], n: int) -> List[int]:
    result = []
    i = 0
    while i < len(lst):
        group = []
        for j in range(i, min(i + n, len(lst))):
            group.insert(0, lst[j])
        result.extend(group)
        i += n
    return result


    
   




from typing import Dict, List

def group_by_length(lst: List[str]) -> Dict[int, List[str]]:
   
    grouped_dict = {}
    for string in lst:
        length = len(string)  
        if length in grouped_dict:
            grouped_dict[length].append(string)
        else:
           
            grouped_dict[length] = [string]
    
    
    return dict(sorted(grouped_dict.items()))


    





   







from typing import Dict, Any

def flatten_dict(nested_dict: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    
    flattened_dict = {}
    
    for key, value in nested_dict.items():
        
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        
        
        if isinstance(value, dict):
            flattened_dict.update(flatten_dict(value, new_key, sep))
        
        
        elif isinstance(value, list):
            for i, item in enumerate(value):
                flattened_dict.update(flatten_dict({f"{key}[{i}]": item}, parent_key, sep))
        
        
        else:
            flattened_dict[new_key] = value
    
    return flattened_dict











from typing import List

def unique_permutations(nums: List[int]) -> List[List[int]]:
    
    
    result = []
    
    
    nums.sort()
    
    def backtrack(perm, remaining):
        if not remaining:
            result.append(perm[:])  
            return
        
        prev = None
        for i in range(len(remaining)):
            
            if remaining[i] == prev:
                continue
            prev = remaining[i]
            
            backtrack(perm + [remaining[i]], remaining[:i] + remaining[i+1:])
    
    
    backtrack([], nums)
    
    return result









import re
from typing import List

def find_all_dates(text: str) -> List[str]:
   
    
    date_patterns = [
        r'\b\d{2}-\d{2}-\d{4}\b',  
        r'\b\d{2}/\d{2}/\d{4}\b',  
        r'\b\d{4}\.\d{2}\.\d{2}\b'  
    ]
    

    all_dates = []
    for pattern in date_patterns:
        matches = re.findall(pattern, text)
        all_dates.extend(matches)
    
    return all_dates








from typing import List

def rotate_and_multiply_matrix(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    
    
    rotated_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - i - 1] = matrix[i][j]

    
    final_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            row_sum = sum(rotated_matrix[i]) - rotated_matrix[i][j]  
            col_sum = sum(row[j] for row in rotated_matrix) - rotated_matrix[i][j]  
            final_matrix[i][j] = row_sum + col_sum
    
    return final_matrix

if __name__ == "__main__":


    lst = input("Enter the list of numbers separated by spaces: ")
    lst = list(map(int, lst.split()))  
    n = int(input("Enter the value of n (group size): "))
    result = reverse_by_n_elements(lst, n)
    print(f"Reversed list by groups of {n}: {result}")





    strings = input("Enter a list of words separated by spaces: ")
    lst = strings.split()  
    result = group_by_length(lst)
    print(f"Grouped strings by length: {result}")



   
    nested_dict = {
        "road": {
            "name": "Highway 1",
            "length": 350,
            "sections": [
                {
                    "id": 1,
                    "condition": {
                        "pavement": "good",
                        "traffic": "moderate"
                    }
                }
            ]
        }
    }
    
    result = flatten_dict(nested_dict)
    print(f"Flattened dictionary: {result}")





    
    nums = [int(x) for x in input("Enter the list of numbers separated by space: ").split()]
    result = unique_permutations(nums)
    print("Unique permutations:")
    for perm in result:
        print(perm)




    
    text = input("Enter the text: ")
    result = find_all_dates(text)
    print("Valid dates found:", result)




    
    matrix = []
    n = int(input("Enter the size of matrix (n x n): "))
    print(f"Enter the {n}x{n} matrix row by row:")
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    result = rotate_and_multiply_matrix(matrix)
    
    print("\nTransformed Matrix:")
    for row in result:
        print(row)












# import pandas as pd

# def time_check(df: pd.DataFrame) -> pd.Series:
    
#     # Convert 'timestamp' columns to datetime
#     df['start'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
#     df['end'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

#     # Create a multi-index DataFrame grouped by ('id', 'id_2')
#     grouped = df.groupby(['id', 'id_2'])

#     # Initialize a boolean series to hold results
#     result = pd.Series(index=grouped.groups.keys(), dtype=bool)

#     for (id_val, id_2_val), group in grouped:
#         # Check if the group covers all 7 days and 24 hours
#         days_covered = group['start'].dt.dayofweek.unique()  # 0=Monday, 6=Sunday
#         full_day_covered = (group['start'].min().date() == group['end'].max().date())
#         all_days = set(range(7))

#         # Check conditions
#         if len(days_covered) == 7 and full_day_covered:
#             result[(id_val, id_2_val)] = True
#         else:
#             result[(id_val, id_2_val)] = False

#     return result

# # Example to read CSV input and run the function
# if _name_ == "_main_":
#     # Load your dataset from a CSV file
#     filename = "dataset-1.csv"
#     df = pd.read_csv(filename)

#     # Call the time_check function and display the output
#     result_series = time_check(df)
#     print(result_series)







