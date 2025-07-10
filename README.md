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

---
# 🌿 CarbonCue API Documentation

This API is built with **FastAPI** to estimate **carbon emissions** across various lifestyle categories using pre-trained ML models.


## 📦 Models Loaded

The following models are loaded from `models/` directory:

- `ModelTransport.pkl`
- `ModelHomeEnergy.pkl`
- `ModelDigitalUsage.pkl`
- `ModelShopping.pkl`
- `ModelFoodDiet.pkl`

---

## 🔐 CORS Support

CORS is enabled to allow frontend applications to communicate with this API. You can customize CORS settings by modifying:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---


---

## 🧩 Schemas (Pydantic Models)

### 🔸 Transport
```python
class Transport(BaseModel):
    transport: Literal["private", "public", "walk/bicycle"]
    vehicle_type: Literal['petrol', 'diesel', 'electric','None']
    vehicle_monthly_distance_km: float
    frequency_of_traveling_by_air: Literal['never', 'rarely', 'frequently', 'very frequently']
```

### 🔸 HomeEnergy
```python
class HomeEnergy(BaseModel):
    heating_energy_source: Literal['electricity','natural gas', 'wood', 'coal','None']
    energy_efficiency: Literal['No','Sometimes','Yes']
    how_long_tv_pc_daily_hour: int
```

### 🔸 DigitalUsage
```python
class DigitalUsage(BaseModel):
    how_long_internet_daily_hour: int
```

### 🔸 Shopping
```python
class Shopping(BaseModel):
    how_many_new_clothes_monthly: int
    waste_bag_size: Literal['small', 'medium', 'large', 'extra large', 'None']
    waste_bag_weekly_count: int
    recycling: List[Literal["Paper", "Plastic", "Glass", "Metal"]] = Field(default_factory=list)
```

### 🔸 FoodDiet
```python
class FoodDiet(BaseModel):
    diet: Literal['vegan', 'vegetarian', 'pescetarian', 'omnivore', 'None']
    monthly_grocery_bill: int
```

---

## 📡 Endpoints

### `GET /`
- **Description:** Root endpoint to check the welcome message.
- **Response:**
```json
{
  "message": "Welcome to the CarbonCue API",
  "status": "healthy"
}
```

---

### `GET /health`
- **Description:** Returns API and model health.
- **Response:**
```json
{
  "status": "healthy",
  "models_loaded": 5
}
```

---

### `POST /predictTransport`
- **Description:** Predict carbon emission from transport data.
- **Request Body:**
```json
{
  "transport": "private",
  "vehicle_type": "petrol",
  "vehicle_monthly_distance_km": 500.0,
  "frequency_of_traveling_by_air": "rarely"
}
```

---

### `POST /predictHomeEnergy`
- **Description:** Predict emission based on home energy use.
- **Request Body:**
```json
{
  "heating_energy_source": "electricity",
  "energy_efficiency": "Yes",
  "how_long_tv_pc_daily_hour": 5
}
```

---

### `POST /predictDigitalUsage`
- **Description:** Predict carbon output from internet use.
- **Request Body:**
```json
{
  "how_long_internet_daily_hour": 6
}
```

---

### `POST /predictShopping`
- **Description:** Predict shopping-related emissions.
- **Request Body:**
```json
{
  "how_many_new_clothes_monthly": 3,
  "waste_bag_size": "medium",
  "waste_bag_weekly_count": 2,
  "recycling": ["Paper", "Plastic"]
}
```

---

### `POST /predictFoodDiet`
- **Description:** Estimate emissions from food and diet.
- **Request Body:**
```json
{
  "diet": "omnivore",
  "monthly_grocery_bill": 500
}
```

---

