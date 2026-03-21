# Session 03 Overview

This folder (`session03`) introduces **regression analysis** as a framework for understanding relationships between variables, alongside **geospatial data analysis** and **financial modelling**. The session moves from descriptive and inferential statistics into predictive modelling, covering simple OLS regression, the Capital Asset Pricing Model (CAPM), and large-scale geospatial data pipelines.

## Data and Statistical Concepts Covered

1. **Simple Linear Regression (OLS)**
   - **World Happiness Report**: Regressing a country's happiness score on GDP per capita, social support, life expectancy, and other well-being indicators.
   - **Model Interpretation**: Reading regression output — coefficients, standard errors, t-statistics, p-values, R², and adjusted R².
   - **Residual Diagnostics**: Assessing model fit via residuals-vs-fitted plots, Q-Q plots, and scale-location plots to check for heteroscedasticity, non-linearity, and outliers.
   - **Prediction**: Generating fitted values and prediction intervals.

2. **Capital Asset Pricing Model (CAPM)**
   - **Beta Estimation**: Regressing a stock's excess returns (above the risk-free rate) on market excess returns to estimate systematic risk (β).
   - **AAPL Case Study**: Downloading Apple and S&P 500 historical prices via `yfinance`, computing log returns, and estimating CAPM beta via OLS.
   - **S&P 500 Constituents**: Extending the CAPM analysis to the full S&P 500 index — estimating beta for every constituent stock.
   - **Alpha & Beta Interpretation**: Understanding what it means for a stock to be defensive (β < 1) or aggressive (β > 1), and whether alpha is statistically significant.

3. **Surge Pricing Analysis (Uber)**
   - Analysing the distribution of Uber surge multipliers by time of day, day of week, and borough.
   - Identifying when and where surge pricing is most extreme using grouped summaries and visualisations.

4. **Geospatial Data Analysis**
   - **NYC Ride-Sharing**: Mapping Uber and Lyft pickup density across New York City boroughs using choropleth maps.
   - **DuckDB Streaming**: Processing large Parquet files with DuckDB SQL queries without loading the full dataset into memory — a pattern essential for big-data workflows.
   - **GeoPandas**: Merging tabular ride data with GeoJSON boundary files to produce choropleth maps.

5. **Concept Check 2 — Salary Discrimination Case Study**
   - Applying regression and two-sample tests to assess whether Winner Plc exhibits gender-based salary discrimination.
   - Using a `sqrt` transformation to address right-skewed salary distributions.
   - Comparing models with and without a gender indicator variable.

## Programming Techniques & Tools

1. **Regression Modelling (`statsmodels`)**
   - `smf.ols('y ~ x1 + x2', data=df).fit()` — R-style formula interface for OLS.
   - `.summary()` — full regression output including coefficient table, F-statistic, and goodness-of-fit measures.
   - `summary_col([m1, m2, m3])` — side-by-side model comparison table.
   - Reusable `fit_and_plot(formula, data)` helper function pattern for iterative model building.

2. **Financial Data (`yfinance`)**
   - `yf.download(tickers, start, end)` — programmatically fetching OHLCV price history for any ticker.
   - Computing log returns and aligning multiple series by date for regression.
   - Risk-free rate adjustment using the 3-month T-bill rate.

3. **Big Data with DuckDB**
   - Writing SQL queries directly in Python against Parquet files using `duckdb.connect()`.
   - Streaming aggregations (group by borough, count rides) without loading millions of rows into RAM.
   - Joining DuckDB query results back to pandas DataFrames for visualisation.

4. **Geospatial Visualisation (`geopandas`, `matplotlib`)**
   - Reading GeoJSON boundary files with `gpd.read_file()`.
   - Merging ride counts onto borough geometries with `.merge()`.
   - Plotting choropleth maps with `.plot(column=..., legend=True)`.

5. **Data Wrangling (`pandas`, `numpy`)**
   - Multi-level column flattening after `yf.download()` returns a `MultiIndex` DataFrame.
   - `.pct_change()` and `np.log()` return calculations.
   - `pd.merge()` for joining financial data series on date index.

6. **Visualisation (`seaborn`, `matplotlib`)**
   - 3-panel regression diagnostic plots (actual vs predicted / residuals vs fitted / Q-Q).
   - Scatter plots with OLS trend line overlay using `sns.regplot()`.
   - Heatmaps of correlation matrices with `sns.heatmap()`.
