# Session 04 Overview

This folder (`session04`) extends regression from Session 03 into **multiple regression** — modelling outcomes using several predictors simultaneously. The session covers the key challenges of real-world regression: detecting and handling multicollinearity, diagnosing model assumptions, applying variable transformations, and selecting the best model from competing specifications.

## Data and Statistical Concepts Covered

1. **Multiple Linear Regression**
   - **Smoking & Birth Weight**: Investigating the effect of maternal smoking on infant birth weight while controlling for confounders (maternal age, weight, height, parity). A classic causal inference problem — does the coefficient on `smoke` represent a causal effect?
   - **Height & Earnings**: Regressing annual earnings on height, controlling for gender, education, and experience. Exploring whether the height premium persists after adding controls.
   - **Credit Card Applications**: Predicting credit card balance from income, credit rating, student status, age, and limit — a prototypical multiple regression application in finance.

2. **Multicollinearity & Variance Inflation Factor (VIF)**
   - **What it is**: When two or more predictors are highly correlated, coefficient estimates become unstable and standard errors inflate.
   - **Detection**: Computing VIF for every predictor; a rule of thumb of VIF > 5–10 signals a problem.
   - **Remedies**: Dropping one of a correlated pair, creating composite indices, or using regularisation.
   - **`compute_vif()` helper**: A reusable function using `variance_inflation_factor` from `statsmodels` to produce a tidy VIF table for any model.

3. **Model Building & Selection**
   - **Incremental model building**: Starting with a simple baseline (one predictor), adding variables one by one, and comparing R², adjusted R², AIC, and BIC at each step.
   - **Adjusted R²**: Why adding variables always increases R² but adjusted R² penalises complexity — the correct metric for comparing models with different numbers of predictors.
   - **`summary_col()`**: Displaying multiple model specifications side by side to see how coefficients change as controls are added (the "table of models" approach standard in academic papers).

4. **Variable Transformations**
   - **Log Transformation**: Applying `np.log()` to right-skewed outcomes (earnings, balance) to reduce heteroscedasticity and improve normality of residuals.
   - **Standardisation**: Mean-centering and scaling predictors to make coefficients comparable across variables with different units.
   - **Ordered Categoricals**: Converting string categories (e.g. education level, ethnicity) to `pd.Categorical(ordered=True)` so they sort correctly in plots and models.

5. **Regression Diagnostics**
   - **Residuals vs Fitted**: Checking for non-linearity and heteroscedasticity — residuals should show no pattern.
   - **Q-Q Plot (Normal Probability Plot)**: Assessing whether residuals follow a normal distribution — points should hug the diagonal line.
   - **Scale-Location Plot**: Checking for constant variance (homoscedasticity) across the fitted value range.
   - **Influential Observations**: Identifying high-leverage or high-influence points (Cook's distance) that disproportionately affect coefficient estimates.

6. **Prediction Intervals vs Confidence Intervals**
   - **CI for the mean response**: Uncertainty around the average prediction for a given x.
   - **PI for individual response**: Wider interval accounting for both model uncertainty and individual-level noise — the correct interval for predicting a single new observation.

## Programming Techniques & Tools

1. **Regression Modelling (`statsmodels`)**
   - `smf.ols('y ~ x1 + x2 + C(categorical)', data=df).fit()` — including categorical predictors with the `C()` wrapper.
   - `.get_prediction(new_data).summary_frame()` — extracting both confidence and prediction intervals for new observations.
   - `summary_col([m1, m2, m3], stars=True)` — publication-style side-by-side model comparison.
   - `variance_inflation_factor(X.values, i)` — computing VIF for the i-th predictor.

2. **Reusable Helper Functions**
   - `compute_vif(formula, data)` — fits a model and returns a DataFrame of VIF values for each predictor.
   - `fit_and_plot(formula, data)` — fits a model, prints the summary, and renders the 3-panel diagnostic plot automatically.
   - These patterns mirror the `favstats_by_group()` style from Session 02: encapsulate repeated workflows into named functions.

3. **Data Wrangling (`pandas`, `numpy`)**
   - `pd.Categorical(ordered=True)` for ordinal variables (education levels, income groups).
   - `.apply(lambda row: ...)` for row-wise feature engineering.
   - Constructing design matrices manually with `sm.add_constant()` for use with `variance_inflation_factor`.

4. **Visualisation (`seaborn`, `matplotlib`)**
   - **3-panel diagnostic layout**: `plt.subplots(1, 3)` with actual-vs-predicted scatter, residuals-vs-fitted scatter, and Q-Q plot side by side.
   - `sm.qqplot(residuals, line='s', ax=ax)` — normal probability plot with standardised line.
   - Scatter plots with prediction interval bands shaded using `ax.fill_between()`.
   - Coefficient plots (dot-and-whisker) to visualise model estimates and CIs.
