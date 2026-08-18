# Model Evaluation Report

## Financial Risk Prediction Using Econometric and Machine Learning Approaches

## 1. Research Objective

This project evaluates machine learning approaches for corporate bankruptcy prediction using financial indicators.

The objective is to compare traditional statistical modeling approaches with advanced ensemble learning methods while maintaining model interpretability through Explainable Artificial Intelligence (XAI).


# 2. Experimental Design

The prediction task was formulated as a binary classification problem:

- 0 = Healthy company
- 1 = Bankrupt company

The dataset contains:

- 6,819 company observations
- 96 original financial indicators
- 76 engineered financial features used for modeling

The dataset was divided into training and testing subsets for model evaluation.


# 3. Models Evaluated

Three classification approaches were implemented:

## Logistic Regression

Used as the econometric baseline model due to its:

- Interpretability
- Statistical foundation
- Ability to estimate bankruptcy probability


## Random Forest

Implemented as an ensemble learning approach capable of:

- Capturing non-linear relationships
- Handling complex financial interactions
- Providing feature importance estimates


## XGBoost

Applied as a gradient boosting approach because of:

- Strong performance on structured financial data
- Regularization capability
- Improved predictive flexibility


# 4. Performance Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---|---|---|---|---|
| Logistic Regression | 96.19% | 30.00% | 13.64% | 18.75% | 86.94% |
| Random Forest | 96.99% | 63.64% | 15.91% | 25.45% | 94.18% |
| XGBoost | 96.99% | 57.14% | 27.27% | 36.92% | 94.08% |


# 5. Key Findings

The results indicate that machine learning models improved predictive discrimination compared with the econometric baseline.

Key observations:

- Ensemble models achieved higher ROC-AUC values than Logistic Regression.
- Random Forest demonstrated strong overall discrimination capability.
- XGBoost achieved the highest recall and F1-score among tested models.
- Machine learning methods captured complex relationships among financial indicators.


# 6. Explainable AI Analysis

SHAP analysis was applied to understand model decisions.

The analysis provides:

- Global feature importance
- Contribution of financial indicators
- Transparency into prediction mechanisms

This improves trust by answering:

> Why was a company classified as financially risky?


# 7. Research Implications

The findings demonstrate potential applications in:

- Corporate financial monitoring
- Early warning systems
- Credit risk assessment
- Investment analysis support
- Financial decision-making systems

The integration of predictive modeling and explainability provides a framework for responsible AI adoption in financial analytics.


# 8. Limitations

Despite strong predictive performance, several limitations should be considered:

## Dataset Limitation

The analysis is based on historical financial indicators. Changes in economic conditions, industry structure, or market environments may affect model generalization.

## Class Imbalance

Bankruptcy events represent a smaller proportion of observations. Therefore, accuracy alone may not fully represent model effectiveness.

## External Validation

Further validation using additional financial datasets and real-world corporate cases would improve generalizability.

## Model Interpretability

Although SHAP improves transparency, complex ensemble models remain less interpretable than traditional econometric approaches.


# 9. Future Research Directions

Future improvements include:

- Time-series financial distress forecasting
- Hyperparameter optimization
- Deep learning approaches
- Alternative financial data integration
- Real-time risk monitoring systems


# Conclusion

This study demonstrates how econometric foundations and machine learning approaches can be combined to develop accurate and interpretable financial risk prediction systems.

The integration of Explainable AI provides a pathway toward transparent and responsible AI-supported financial decision-making.
