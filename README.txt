## Multiple Curve Construction Study - €STR and Euribor

### Table of Contents
- Overview
- Section 1: Data Import and Preparation
- Section 2: Convert Maturities and Set Evaluation Date
- Section 3: Building the €STR Discount Curve
- Section 4: ECB Liquidity Check for Short-Term Rate Analysis
- Section 5: Construction of the 3-Month Euribor Curve - No Synthetic Deposits
- Section 6: Calculation of Basis and Creation of Synthetic Deposits
- Section 7: Construction of the Euribor3M Forward Curve with Synthetic Deposits
- Section 8: Comparing Forward Euribor Curves With and Without Synthetic Deposits
- Section 9: Comparison of Dual Curve and Single Euribor3M Forward Curves - Discounting Impact
- Section 10: Construction of the Euribor6M Forward Curve and Comparison with the Euribor3M Forward Curve - The Importance of Being Tenor Consistent
- Section 11: Constructing and Evaluating Euribor3M Forward Curves via Diverse Bootstrapping Instrument Configurations
- Section 12: Stability Assessment of Bootstrapping Sets

### Overview
This study constructs multiple interest rate curves for €STR and Euribor using various instrument sets. The methodology is based on Ametrano and Bianchetti’s work, implemented in Python with QuantLib. Data is sourced as a snapshot from Refinitiv, up-to-date as of July 13, 2024.

### Section 1: Data Import and Preparation
This section imports necessary libraries and reads data from specified files. The data is processed to calculate mid rates.

### Section 2: Convert Maturities and Set Evaluation Date
Functions are defined to convert maturity strings into QuantLib periods, process the dataset, and set the evaluation date for calculations.

### Section 3: Building the €STR Discount Curve
This section builds the €STR discount curve using selected deposits, OIS pre-ECB, forward OIS ECB, and OIS post-ECB data, with an option to visualize the yield curve.

### Section 4: ECB Liquidity Check for Short-Term Rate Analysis
We analyze short-term rate changes by using flat forward rates and comparing €STR forward rates with ECB forward rates to detect potential liquidity jumps.

### Section 5: Construction of the 3-Month Euribor Curve - No Synthetic Deposits
This section constructs the 3-month Euribor curve without synthetic deposits, including FRA, futures, and swap rate helpers.

### Section 6: Calculation of Basis and Creation of Synthetic Deposits
We calculate the basis (spread) between the forward 3-month Euribor and €STR rates, and create synthetic deposit helpers for accurate Euribor curve construction.

### Section 7: Construction of the Euribor3M Forward Curve with Synthetic Deposits
This section builds the Euribor3M forward curve using synthetic deposits, FRA, futures, and swaps, and visualizes the resulting forward rates.

### Section 8: Comparing Forward Euribor Curves With and Without Synthetic Deposits
A detailed analysis comparing forward Euribor curves with and without synthetic deposits, focusing on short-term rate projections and basis point differences.

### Section 9: Comparison of Dual Curve and Single Euribor3M Forward Curves - Discounting Impact
We construct Euribor curves using both dual and single curve approaches, comparing zero and forward rates to highlight differences in future rate expectations.

### Section 10: Construction of the Euribor6M Forward Curve and Comparison with the Euribor3M Forward Curve - The Importance of Being Tenor Consistent
This section constructs the Euribor6M forward curve and compares it with the Euribor3M forward curve to identify differences between the two.

### Section 11: Constructing and Evaluating Euribor3M Forward Curves via Diverse Bootstrapping Instrument Configurations
We develop and evaluate Euribor3M forward curves using various bootstrapping configurations, comparing structural variations and rate projections.

### Section 12: Stability Assessment of Bootstrapping Sets
This section assesses the stability of Euribor3M forward curve bootstrapping sets under simulated market shocks, analyzing tracking errors and curve sensitivity.


