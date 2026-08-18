# Explainable AI for Corporate Bankruptcy Prediction: Integrating Econometric and Machine Learning Approaches

## Abstract

Corporate bankruptcy prediction is a critical challenge in financial analytics, risk management, and strategic decision-making. Early identification of financially distressed companies enables investors, financial institutions, regulators, and managers to take preventive actions.

This project develops an interpretable machine learning framework for corporate bankruptcy prediction using financial indicators. The study evaluates traditional statistical modelling and advanced machine learning approaches by comparing Logistic Regression, Random Forest, and XGBoost models.

Using a dataset containing 6,819 corporate observations and 96 financial indicators, the models are evaluated using accuracy, precision, recall, F1-score, and ROC-AUC metrics. Explainable Artificial Intelligence (XAI) techniques using SHAP analysis are applied to improve model transparency and identify influential financial factors associated with bankruptcy risk.

The results demonstrate that ensemble machine learning approaches provide stronger predictive capability compared with traditional statistical baselines while maintaining interpretability through explainable AI methods.

---

# 1. Executive Summary

Financial distress prediction plays an important role in modern financial decision-making. Traditional econometric models have been widely applied for bankruptcy prediction; however, complex financial relationships may require advanced machine learning techniques capable of capturing nonlinear patterns.

This research project develops a reproducible artificial intelligence framework that combines financial analytics, machine learning, and explainable AI to predict corporate bankruptcy risk.

The study compares:

- Logistic Regression as an interpretable statistical baseline.
- Random Forest as an ensemble learning approach.
- XGBoost as an advanced gradient boosting model.

The framework emphasizes both predictive performance and model transparency to support trustworthy AI adoption in financial risk management.

---

# 2. Research Objectives

This study addresses three main objectives:

1. Evaluate whether machine learning models improve bankruptcy risk prediction compared with traditional statistical approaches.

2. Identify important financial indicators associated with corporate financial distress.

3. Apply Explainable AI techniques to improve transparency and interpretability of machine learning predictions.

---

# 3. Research Contribution

This project contributes to financial analytics research by integrating:

- Econometric modelling principles with modern machine learning methods.
- Predictive modelling with Explainable Artificial Intelligence techniques.
- Financial risk assessment with transparent decision-support approaches.

Unlike purely predictive black-box systems, this framework focuses on balancing predictive accuracy with interpretability, supporting responsible AI applications in financial decision-making.

---

# 4. Dataset and Methodology

## Dataset Description

The analysis uses a corporate bankruptcy dataset containing financial indicators of companies.

Dataset characteristics:

| Attribute | Description |
|---|---|
| Observations | 6,819 companies |
| Features | 96 financial indicators |
| Target Variable | Bankruptcy status |

Target classification:
0 = Healthy company
1 = Bankruptcy risk


The financial variables represent multiple dimensions including:

- Profitability
- Liquidity
- Leverage
- Efficiency
- Asset utilization
- Financial stability

---

# 5. Analytical Framework

The project follows a complete reproducible machine learning workflow:

Financial Dataset
|
↓
Data Preparation
|
↓
Exploratory Data Analysis
|
↓
Feature Processing
|
↓
Machine Learning Models
|
↓
Performance Evaluation
|
↓
Explainable AI Analysis
|
↓
Financial Risk Insights

---

# 6. Machine Learning Models

## Logistic Regression

Logistic Regression was implemented as a traditional econometric baseline due to its interpretability and extensive application in financial distress prediction research.

## Random Forest

Random Forest was applied to capture complex relationships and nonlinear interactions among financial variables.

## XGBoost

XGBoost was implemented as an advanced gradient boosting algorithm due to its strong performance on structured financial datasets.

---

# 7. Model Evaluation Results

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 96.19% | 30.00% | 13.64% | 18.75% | 85.23% |
| Random Forest | 96.92% | 60.00% | 13.64% | 22.22% | 93.80% |
| XGBoost | 97.29% | 65.22% | 34.09% | 44.78% | 94.72% |

---

# 8. Key Research Findings

## Finding 1: Ensemble Models Improve Prediction Performance

The results indicate that ensemble learning methods outperform traditional statistical modelling approaches.

XGBoost achieved the strongest overall performance, demonstrating the ability of machine learning algorithms to capture complex relationships among financial indicators.

---

## Finding 2: Accuracy Alone is Insufficient

Although the models achieved high accuracy, bankruptcy prediction requires careful consideration of recall and F1-score because financially distressed companies represent a minority class.

Therefore, effective risk prediction systems should prioritize early detection capability rather than accuracy alone.

---

## Finding 3: Explainable AI Improves Transparency

SHAP analysis provides insights into how financial indicators influence model predictions.

This improves trust, interpretability, and practical adoption of AI-based financial risk systems.

---

# 9. Explainable AI Analysis

Explainable Artificial Intelligence techniques were applied to understand model behaviour and identify important predictors.

The analysis includes:

- SHAP feature importance
- Feature contribution analysis
- Model interpretation

These approaches help transform machine learning predictions into actionable financial insights.

---

# 10. Practical Applications

The proposed framework can support multiple stakeholders.

## Financial Institutions

Applications include:

- Credit risk assessment
- Loan portfolio monitoring
- Early warning systems

## Investors

Applications include:

- Corporate risk screening
- Investment decision support

## Regulators

Applications include:

- Financial stability monitoring
- Identification of vulnerable companies and sectors

## Corporate Managers

Applications include:

- Internal financial health assessment
- Strategic risk management

---

# 11. Managerial and Policy Implications

The findings suggest that artificial intelligence should complement traditional financial analysis rather than replace expert judgement.

Organizations should:

- Combine AI predictions with financial expertise.
- Use explainable models for transparent decision-making.
- Develop continuous monitoring systems for financial risks.
- Update models as economic conditions change.

---

# 12. Limitations

This study has several limitations:

- The dataset represents historical financial information and may not capture future market conditions.
- Macroeconomic factors such as inflation, interest rates, and market shocks are not included.
- Model performance depends on data quality and feature availability.
- Additional validation using longitudinal financial data is required.

---

# 13. Future Research Directions

Future research may explore:

- Time-series bankruptcy forecasting.
- Deep learning architectures.
- Integration of macro-financial indicators.
- Real-time financial risk monitoring.
- Automated financial decision-support systems.

---

# 14. Conclusion

This project demonstrates the potential of combining econometric foundations, machine learning algorithms, and Explainable AI techniques for corporate bankruptcy prediction.

The proposed framework provides both predictive capability and interpretability, supporting the development of trustworthy AI applications in financial analytics and risk management.

---

# References

Detailed academic references, datasets, and technical resources are available in:

[REFERENCES.md](../REFERENCES.md)

---

# Reproducibility

The complete pipeline can be reproduced using:

```bash
python -m src.train
