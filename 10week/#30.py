choi = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

result= {key: value for key, value in choi.items() if value >=90}
print(result)