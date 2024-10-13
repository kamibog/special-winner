import requests
import matplotlib.pyplot as plt
import pandas as pd

response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    data = response.json()
    print(data[:5])
else:
    print(f"Ошибка: {response.status_code}")



"""x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title('Пример графика')
plt.xlabel('X-ось')
plt.ylabel('Y-ось')
plt.grid()
plt.show()"""




"""data = pd.read_csv('data.csv')

print(data.head())

mean_value = data['value'].mean()
print(f'Mean Value: {mean_value}')"""
