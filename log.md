# 專案操作紀錄

此檔案用於記錄在本專案 (hw1) 中由 GitHub Copilot 執行的所有步驟。

---

- 2025-09-24 建立 log.md 以紀錄專案操作。

- 2025-09-24 依據 CRISP-DM 方法論，建立 `streamlit_app.py`，內容包含：
prompt:"
You are tasked to write Python code and explanation for a homework project. 
Follow CRISP-DM steps (Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment). 
Do NOT only output code and results. You must include prompts, reasoning steps, and CRISP-DM methodology descriptions as markdown text mixed with code. 

Requirements:
1. Data Generation:
   - Generate n data points (x, y), where n is a user-selectable integer between 100 and 1000.
   - Relationship: y = a * x + b + noise
   - a: user-selectable coefficient between -10 and 10
   - b: you can set as a constant, e.g., b = 5
   - noise: Normally distributed noise N(0, var), with var selectable between 0 and 1000
2. Linear Regression Visualization:
   - Plot generated data points
   - Draw regression line in red
3. Outlier Identification:
   - Identify the top 5 outliers (points furthest from regression line)
   - Mark and label them on the plot
4. User Interface:
   - Use Streamlit (preferred) or Flask for deployment
   - Provide sliders/input fields for users to control parameters: n, a, var
   - Display plot, regression line, and regression results (slope, intercept, R² score)
   - Clearly show CRISP-DM steps in the UI or as markdown text

Output requirements:
- Write a Streamlit app
- Include markdown explanations for each CRISP-DM step
- Show the process clearly, not only the final code and result
- Explanations should be educational and detailed, as if explaining to students

Deliverables:
- Python code with comments
- Streamlit interface implementation
- Markdown explanations integrated into the app
"

  1.  Business Understanding：說明專案目標與學習重點
  2.  Data Understanding：解釋資料生成方式與參數意義
  3.  Data Preparation：產生資料並檢查型態與分布
  4.  Modeling：以 sklearn 線性回歸建模，顯示斜率、截距、R²
  5.  Evaluation：根據殘差找出離群值並視覺化
  6.  Deployment：以 Streamlit 部署，支援互動式參數調整與即時視覺化
  - 介面整合 markdown 說明與互動元件，適合教學與自學
  - 已完成初版程式設計與說明整合
