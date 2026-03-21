# Session 02 Overview

This folder (`session02`) builds on the foundational statistics from Session 01 by introducing **inferential statistics** — moving from describing data to drawing conclusions and testing hypotheses. The session covers hypothesis testing, confidence intervals, A/B experimentation, and time series analysis of financial data, all grounded in real-world datasets.

## Data and Statistical Concepts Covered

1. **Hypothesis Testing & Confidence Intervals**
   - **One-Sample t-Test**: Testing whether a population mean differs from a known benchmark (e.g. does global temperature anomaly differ from a pre-industrial baseline?).
   - **Two-Sample Welch's t-Test**: Comparing means between two independent groups without assuming equal variances (e.g. credit balances by gender, student pulse rates by exercise level).
   - **Confidence Intervals**: Constructing CIs for single means and for the *difference* between two means using the t-distribution (`scipy.stats.t.interval`), including the standard error formula for each case.
   - **Statistical Significance vs Practical Significance**: Interpreting p-values cautiously alongside effect sizes and CIs.

2. **A/B Testing**
   - **Experimental Design**: Separating a treatment group (new app feature) from a control group; understanding randomisation and its role in causal inference.
   - **Uber Ride Data**: Analysing whether a new driver incentive scheme affected trips per driver — visualising pre/post trends and applying Welch's t-test to detect a statistically significant lift.

3. **Exploratory Data Analysis with Categorical Variables**
   - Comparing distributions across groups (income, gender, card type) using overlapping histograms, density plots, stripplots, and pointplots with error bars.
   - Summarising grouped data with custom `favstats`-style tables (mean, SD, n, SE, CI bounds).

4. **Climate Data Analysis**
   - **LOWESS Smoothing**: Fitting a locally weighted regression curve to noisy temperature anomaly data to reveal long-run trends.
   - **Ordered Categorical Time Periods**: Classifying years into eras and comparing distributions with ECDF plots and the 1.5 °C threshold.

5. **Financial Time Series & Risk**
   - **Simple vs Log Returns**: Understanding the difference, when to use each, and their mathematical relationship.
   - **Risk Metrics**: Annualised volatility (standard deviation of log returns × √252), Sharpe ratio, maximum drawdown.
   - **Total Return Index**: Compounding returns from a base of 100 to compare assets on the same scale.
   - **Benchmarking**: Using SPY (S&P 500 ETF) as a market benchmark alongside individual DJIA stocks.

## Programming Techniques & Tools

1. **Data Wrangling (`pandas`, `numpy`)**
   - **Wide → Long Reshaping**: `pd.melt()` to transform multi-column datasets (e.g. one column per year) into tidy long format ready for `groupby` and `seaborn`.
   - **Ordered Categoricals**: `pd.Categorical(..., ordered=True)` to control sort order in `groupby` and plot axes.
   - **Time Series Resampling**: `.resample('ME').last()` to downsample daily prices to month-end, then `.pct_change()` for simple returns.
   - **Log Returns**: `np.log(x / x.shift(1))` — the standard formula for continuously compounded returns.
   - **Cumulative Returns**: `(1 + r).cumprod() * 100` to build a total return index from a base of 100.

2. **Web Scraping & API Data Collection**
   - **`requests` + `BeautifulSoup`**: Fetching and parsing HTML tables from the web (e.g. DJIA constituent list from Wikipedia).
   - **`pd.read_html()`**: Quickly parsing HTML tables into DataFrames without writing a custom parser.
   - **`response.raise_for_status()`**: Best-practice error handling for HTTP requests.

3. **Statistical Computing (`scipy.stats`, `statsmodels`)**
   - `stats.ttest_1samp()` — one-sample t-test.
   - `stats.ttest_ind(equal_var=False)` — Welch's two-sample t-test.
   - `stats.t.interval()` and `stats.sem()` — confidence interval construction.
   - `statsmodels.nonparametric.smoothers_lowess.lowess` — LOWESS curve fitting.

4. **Visualisation (`matplotlib`, `seaborn`)**
   - **Layered plots**: combining `sns.stripplot()` and `sns.pointplot()` on the same `ax` to show both individual data points and group means with CIs.
   - **FacetGrid with `row=`**: Creating small-multiple panels split by an ordered categorical variable.
   - **ECDF plots**: Looping over groups, plotting empirical CDFs, adding `axvline` for reference thresholds, and formatting y-axis as percentages with `PercentFormatter`.
   - **Time series**: Plotting price and return series with appropriate axis formatting.
