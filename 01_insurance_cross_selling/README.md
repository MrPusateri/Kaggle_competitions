# Introduction

This article aims to present how to menage an unbalanced data-set for a classification problem. In particular, the article present three classification models using the `XGBClassifier` of the _XGBoost_ Python library. The main differences between models are:
1. Train without parameters to balance data.
2. Train with parameter to balance data. The parameter `scale_pos_weight`, control the balance of positive and negative weights, useful for unbalanced classes. A typical value to consider: `sum(negative instances) / sum(positive instances)`. 
3. Train the model with balanced data using `SMOTENC` method to oversampling data.