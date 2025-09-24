"""
streamlit_app.py

本檔案為作業專案主程式，依據 CRISP-DM 方法論，結合互動式 Streamlit 介面，實現資料生成、線性回歸、離群值偵測與視覺化。
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# --- CRISP-DM 步驟說明 ---

st.title('CRISP-DM 線性回歸互動專案')

st.markdown('''
# 1. Business Understanding (業務理解)
本專案目標：
- 透過模擬線性資料，讓學生理解線性回歸、離群值偵測與資料分析流程。
- 以互動方式體驗資料科學專案的 CRISP-DM 步驟。
''')

st.markdown('''
# 2. Data Understanding (資料理解)
- 資料由 $y = a \times x + b + \text{noise}$ 生成。
- 你可調整資料點數 (n)、斜率 (a)、雜訊變異數 (var)。
- b 固定為 5。
''')

# --- 參數輸入 ---
st.sidebar.header('參數設定')
n = st.sidebar.slider('資料點數 n', min_value=100, max_value=1000, value=300, step=10)
a = st.sidebar.slider('斜率 a', min_value=-10.0, max_value=10.0, value=2.0, step=0.1)
var = st.sidebar.slider('雜訊變異數 var', min_value=0.0, max_value=1000.0, value=100.0, step=1.0)
b = 5

# --- 資料生成 ---
np.random.seed(42)
x = np.linspace(-50, 50, n)
noise = np.random.normal(0, np.sqrt(var), n)
y = a * x + b + noise

st.markdown('''
# 3. Data Preparation (資料準備)
- 產生 $x$、$y$ 資料，並加入常態分布雜訊。
- 檢查資料型態與分布。
''')

st.write('前 5 筆資料：')
st.write({'x': x[:5], 'y': y[:5]})

# --- 建立回歸模型 ---
X = x.reshape(-1, 1)
reg = LinearRegression()
reg.fit(X, y)
y_pred = reg.predict(X)
r2 = r2_score(y, y_pred)

st.markdown('''
# 4. Modeling (建模)
- 使用 sklearn 線性回歸模型擬合資料。
- 顯示回歸線、斜率、截距與 $R^2$ 分數。
''')

st.write(f'回歸斜率 (slope): {reg.coef_[0]:.3f}')
st.write(f'回歸截距 (intercept): {reg.intercept_:.3f}')
st.write(f'R² 分數: {r2:.3f}')

# --- 離群值偵測 ---
residuals = np.abs(y - y_pred)
outlier_indices = np.argsort(residuals)[-5:][::-1]

st.markdown('''
# 5. Evaluation (評估)
- 根據殘差找出離群值 (距離回歸線最遠的 5 點)。
- 在圖上標註離群值。
''')

# --- 視覺化 ---
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(x, y, label='資料點', alpha=0.6)
ax.plot(x, y_pred, color='red', label='回歸線')
ax.scatter(x[outlier_indices], y[outlier_indices], color='orange', s=80, label='離群值')
for idx in outlier_indices:
    ax.annotate(f'Outlier', (x[idx], y[idx]), textcoords="offset points", xytext=(0,10), ha='center', color='orange')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
st.pyplot(fig)

st.markdown('''
# 6. Deployment (部署)
- 本應用以 Streamlit 部署，支援互動式參數調整與即時視覺化。
- 可作為教學、展示或自我練習之用。
''')

st.info('本專案完整展示 CRISP-DM 流程，歡迎調整參數觀察結果變化！')
