# импортируем библиотеку streamlit
import streamlit as st

# Запрос числа у пользователя
number = st.slider('x')

# Вычисление квадрата числа
square = number * number

# Вывод результата
st.write('Квадрат числа ', number, ' равен ', square)
