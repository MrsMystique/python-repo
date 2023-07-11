
### пошаговое руководство по расчетам всех видов регрессий на python 

---


1. Импорт библиотек

Перед началом работы необходимо импортировать необходимые библиотеки для работы со статистическими расчетами на Python, такие как pandas, numpy и sklearn.

```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
```

2. Подготовка данных

Для работы с регрессионными моделями необходимо подготовить данные, например, обработать пропущенные значения, выбросы и провести кодирование категориальных переменных.

```python
# чтение данных из файла
data = pd.read_csv('data.csv')

# проверка на пропущенные значения
data.isnull().sum()

# удаление строк с пропущенными значениями
data = data.dropna()

# разделение данных на независимые и зависимые переменные
X = data.drop('y', axis=1)
y = data['y']

# кодирование категориальных переменных
X = pd.get_dummies(X, drop_first=True)
```

3. Множественная линейная регрессия

Для расчета множественной линейной регрессии необходимо создать объект модели и обучить ее на подготовленных данных.

```python
# разделение данных на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# создание модели
model = LinearRegression()

# обучение модели на тренировочных данных
model.fit(X_train, y_train)

# предсказание результатов на тестовых данных
y_pred = model.predict(X_test)

# оценка качества модели
mse = mean_squared_error(y_test, y_pred)
```

4. Полиномиальная регрессия

Для расчета полиномиальной регрессии необходимо создать объект модели и применить полиномиальные преобразования к независимым переменным.

```python
# создание объекта полиномиальных преобразований
poly = PolynomialFeatures(degree=2)

# применение полиномиального преобразования к независимым переменным
X_poly = poly.fit_transform(X)

# разделение данных на тренировочный и тестовый наборы
X_poly_train, X_poly_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.3, random_state=42)

# создание модели
model = LinearRegression()

# обучение модели на тренировочных данных
model.fit(X_poly_train, y_train)

# применение полиномиального преобразования к тестовым данным
X_poly_test = poly.transform(X_test)

# предсказание результатов на тестовых данных
y_poly_pred = model.predict(X_poly_test)

# оценка качества модели
mse = mean_squared_error(y_test, y_poly_pred)
```

5. Логистическая регрессия

Логистическая регрессия используется для бинарной классификации. Для ее расчета необходимо создать объект модели и обучить ее на подготовленных данных.

```python
# создание модели
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()

# разделение данных на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# обучение модели на тренировочных данных
logreg.fit(X_train, y_train)

# предсказание результатов на тестовых данных
y_pred = logreg.predict(X_test)

# оценка качества модели
from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
```

---

