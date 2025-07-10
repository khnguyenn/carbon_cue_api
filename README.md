# 🧮 Carbon Emission Category Split Analysis

This document presents a comparative analysis of carbon emission attribution across five categories using **three methods**:  
1. **Percentage-based Splits**  
2. **Feature Importance Splits**  
3. **Regression-based Splits**  
Then combines them into a **hybrid approach**.

---

## 📊 1. Percentage-Based Method

**Original Total Mean**: `2269.15`  
**Sum of Category Means**: `2269.15`  
**Difference**: `0.00`

| Category        | Percentage | Emission (Mean ± SD)     |
|----------------|------------|---------------------------|
| Transportation | 29.0%      | 658.05 ± 295.13           |
| Home_Energy    | 28.0%      | 635.36 ± 284.95           |
| Food_Diet      | 23.0%      | 521.90 ± 234.07           |
| Shopping       | 15.0%      | 340.37 ± 152.65           |
| Digital_Usage  | 5.0%       | 113.46 ± 50.88            |

---

## 🌲 2. Feature Importance-Based Method

Trained on a Random Forest model to determine top features and aggregate importance per category.

### 🔝 Top 10 Features by Importance:
| Feature                          | Importance |
|----------------------------------|------------|
| Vehicle Type                     | 0.3448     |
| Vehicle Monthly Distance Km      | 0.3063     |
| Frequency of Traveling by Air    | 0.1686     |
| How Many New Clothes Monthly     | 0.0460     |
| Monthly Grocery Bill             | 0.0220     |
| Waste Bag Weekly Count           | 0.0213     |
| How Long Internet Daily Hour     | 0.0153     |
| Waste Bag Size                   | 0.0152     |
| Recycling                        | 0.0145     |
| How Long TV PC Daily Hour        | 0.0137     |

### 📈 Category Percentages Based on Feature Importance:
| Category        | Percentage |
|----------------|------------|
| Transportation | 82.0%      |
| Home_Energy    | 3.9%       |
| Food_Diet      | 2.9%       |
| Shopping       | 9.7%       |
| Digital_Usage  | 1.5%       |

---

## 📈 3. Regression-Based Method

Each category was trained independently using Random Forest models. R² scores were normalized to reflect each category's contribution.

### 🧪 Model R² Scores:
| Category        | R² Score | Sample Size |
|----------------|----------|-------------|
| Transportation | 0.916    | 3279        |
| Home_Energy    | 0.306    | 10000       |
| Food_Diet      | 0.080    | 10000       |
| Shopping       | 0.573    | 10000       |
| Digital_Usage  | 0.003    | 10000       |

### 🧾 Regression-Based Percentages:
| Category        | Percentage |
|----------------|------------|
| Transportation | 48.8%      |
| Home_Energy    | 16.3%      |
| Food_Diet      | 4.3%       |
| Shopping       | 30.5%      |
| Digital_Usage  | 0.1%       |

---

## 🔀 Final Hybrid Approach (Weighted Combination)

Weights used:
- Percentage-Based: **40%**
- Feature Importance-Based: **30%**
- Regression-Based: **30%**

### ✅ Final Normalized Hybrid Percentages:
| Category        | Final %    |
|----------------|------------|
| Transportation | **50.8%**  |
| Home_Energy    | **17.2%**  |
| Food_Diet      | **11.4%**  |
| Shopping       | **18.1%**  |
| Digital_Usage  | **2.5%**   |
