# Group Project Overview

This folder (`group_project`) contains the capstone data analytics project for the programme. The project applies the full toolkit developed across Sessions 01–04 to a real-world dataset: **London's TfL (Transport for London) Bike Sharing scheme**. The goal is to understand the factors that drive daily bike hire volumes and build a regression model that can explain and predict demand.

## Data and Statistical Concepts Covered

1. **Exploratory Data Analysis (EDA)**
   - **Summary Statistics**: Distribution of daily hires — mean, median, standard deviation, skewness; identifying outliers and anomalies.
   - **Temporal Patterns**: How demand varies by day of week, month, season, and year. Using `dt` accessor methods to extract date components.
   - **Weather Effects**: Quantifying the relationship between temperature, wind speed, humidity, and bike hire volumes — both visually and via correlation analysis.
   - **Categorical Breakdowns**: Comparing hire volumes across seasons, weekdays vs weekends, and holiday vs non-holiday days.

2. **Multiple Linear Regression**
   - Building an OLS model to predict daily bike hires from weather variables, day-type indicators (weekend, holiday), and seasonal dummies.
   - **Incremental model building**: Starting simple (temperature only), then adding weather variables, then calendar variables, comparing adjusted R² and AIC at each step.
   - **Interaction Terms**: Testing whether the effect of temperature on demand differs between summer and winter, or between weekdays and weekends.

3. **Variable Transformations**
   - Addressing right-skewed demand distribution with a log transformation of the outcome variable.
   - `np.select()` / `pd.Categorical()` to create ordered season and day-of-week variables from raw date data.
   - Boolean indicators from `.dt.day_name().isin(['Saturday', 'Sunday'])` for weekend flag.

4. **Model Diagnostics & Selection**
   - Residuals-vs-fitted, Q-Q plot, and scale-location plots to validate model assumptions.
   - VIF analysis to check for multicollinearity between weather variables (temperature and humidity are often correlated).
   - Comparing nested models with `summary_col()` in a presentation-ready table.

5. **Prediction**
   - Generating predictions for new scenarios (e.g. a sunny weekend in July vs a rainy Monday in January).
   - Constructing prediction intervals to communicate uncertainty around point forecasts.

## Programming Techniques & Tools

1. **Data Loading & Cleaning (`pandas`)**
   - Reading data from a remote URL with `pd.read_csv()`.
   - Parsing date columns with `pd.to_datetime()` and using the `.dt` accessor for feature engineering (year, month, day name, season).
   - Method chaining with `.assign()` to build a clean pipeline from raw CSV to analysis-ready DataFrame.
   - `pd.Categorical(ordered=True)` for season and day-of-week variables.

2. **Regression Modelling (`statsmodels`)**
   - `smf.ols('cnt ~ temp + hum + windspeed + C(season)', data=bike).fit()` — R-style formula API including categorical dummies.
   - `summary_col([m1, m2, m3], stars=True)` — side-by-side model comparison table.
   - `variance_inflation_factor` — checking multicollinearity among weather predictors.
   - `.get_prediction().summary_frame()` — confidence and prediction intervals for new data.

3. **Visualisation (`seaborn`, `matplotlib`)**
   - Scatter plots and regression lines for continuous predictors (temperature, wind speed).
   - Boxplots and violin plots for categorical predictors (season, weekday/weekend).
   - Time series line plots of daily and monthly hire volumes.
   - 3-panel diagnostic plot (actual vs predicted / residuals vs fitted / Q-Q).
   - Correlation heatmap with `sns.heatmap(df.corr())`.

4. **Statistical Computing (`scipy.stats`)**
   - Correlation tests (`pearsonr`, `spearmanr`) to quantify strength of relationships before modelling.
   - Normality tests on model residuals.
