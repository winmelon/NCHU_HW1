# NCHU_HW1

本專案為線性回歸與資料分析互動式教學平台，依據 CRISP-DM 方法論設計，並以 Streamlit 部署。

## 專案特色
- 依據 CRISP-DM 步驟，完整展示資料科學專案流程
- 可自訂資料點數、斜率、雜訊等參數，動態生成資料
- 線性回歸建模與視覺化，並自動標註離群值
- 介面整合 markdown 教學說明，適合自學與教學

## 使用方式
1. 安裝必要套件：
   ```bash
   pip install streamlit scikit-learn matplotlib numpy
   ```
2. 啟動應用程式：
   ```bash
   streamlit run streamlit_app.py
   ```
3. 於瀏覽器操作互動式介面，體驗 CRISP-DM 流程

## 主要檔案說明
- `streamlit_app.py`：主程式，整合互動介面與分析流程
- `log.md`：所有專案操作與重要步驟紀錄
- `README.md`：本說明文件

## CRISP-DM 步驟簡介
1. **Business Understanding**：明確定義專案目標與學習重點
2. **Data Understanding**：說明資料來源、型態與分布
3. **Data Preparation**：資料生成、檢查與前處理
4. **Modeling**：建立線性回歸模型並視覺化
5. **Evaluation**：評估模型、偵測離群值
6. **Deployment**：以 Streamlit 部署，支援互動操作

---

如有問題請聯絡專案負責人。
