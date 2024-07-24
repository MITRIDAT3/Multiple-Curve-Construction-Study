## Multiple Curve Construction Study
# Table of Contents
- Overview
- Data Loading
- Maturity Conversion and Evaluation Date
- €STR Discount Curve Construction
- ECB Liquidity Check Jumps
- Construction of the 3-Month Euribor Curve - No Synthetic Deposits
- Construction of the 3-Month Euribor Curve - With Synthetic Deposits
- Corrected 3M and 6M Euribor Curve Construction
- Construction of the Forward Euribor3M Curve Using Single Curve
- Comparison of Dual Curve and Single Euribor3M Forward Curves
- Construction of the Euribor6M Forward Curve and Comparison with the Euribor3M Forward Curve
- Building and Comparing Different Euribor3M Forward Curves with Different Instrument Bootstrapping Sets
- Stability Comparison between Different Bootstrapping Sets
- Usage
- Contributing
- License
- Future Work
  
# Overview
This study aims to construct multiple interest rate curves for €STR and Euribor using different sets of instruments. The methodology follows the work by Ametrano and Bianchetti, implemented in Python with QuantLib.

# Data Loading
This section imports the necessary libraries and reads data from the specified files. It processes the data to calculate the mid rates, which are the average of the bid and ask prices.

# Maturity Conversion and Evaluation Date
This section defines functions to convert maturity strings into QuantLib periods and processes the dataset to include these periods. It also sets up necessary adjustments for ECB maintenance periods and futures maturities, and defines specific maturities based on the Ametrano and Bianchetti study. The evaluation date for all calculations is set at the end.

# €STR Discount Curve Construction
This section defines a function to build the €STR discount curve. It initializes the curve with selected deposits, OIS pre-ECB, forward OIS ECB, and OIS post-ECB data. The function also includes an option to visualize the resulting yield curve.

# ECB Liquidity Check Jumps
In this section, we perform an ECB liquidity check for potential jumps due to ECB deadlines. By turning to flat forward rates instead of log-cubic discounts, we simplify the analysis and focus on the short-term forward rates over the first six months. The forward curve is plotted to identify any significant liquidity jumps.

# Construction of the 3-Month Euribor Curve - No Synthetic Deposits
In this section, we construct the 3-month Euribor curve without using synthetic deposits. This involves defining the 3-month Euribor instance, adding deposit, futures, and swap rate helpers, and building both the spot and forward curves. The forward curve is then plotted to visualize the 3-month Euribor rates.

# Construction of the 3-Month Euribor Curve - With Synthetic Deposits
In this section, we construct the 3-month Euribor curve using synthetic deposits. This involves defining the 3-month Euribor instance, adding synthetic deposit helpers, and combining them with the original deposit, futures, and swap rate helpers to build both the spot and forward curves. The forward curve is then plotted to visualize the 3-month Euribor rates.

# Corrected 3M and 6M Euribor Curve Construction
This section covers the construction of the corrected 3M and 6M Euribor curves using synthetic deposits. Synthetic deposit rate helpers are created by adjusting the forward rates derived from the €STR curve with a calculated spread (alpha). These synthetic helpers, along with the original deposit, FRA, and SWAP helpers, are used to construct the corrected Euribor curves.

# Construction of the Forward Euribor3M Curve Using Single Curve
In this section, we construct the forward Euribor curve using a single curve approach. We add the necessary swap helpers and combine them with synthetic deposit helpers, deposit helpers, and futures helpers. The resulting single curve forward Euribor curve is then plotted to visualize the forward rates.

# Comparison of Dual Curve and Single Euribor3M Forward Curves
In this section, we calculate the basis point differences between the dual curve and single curve zero and forward Euribor curves. We plot these differences to visualize the comparison between the two approaches.

# Construction of the Euribor6M Forward Curve and Comparison with the Euribor3M Forward Curve
In this section, we construct the forward Euribor6M curve using the dual curve approach. We then compare the Euribor6M forward curve with the Euribor3M forward curve to identify any differences between the two curves.

# Building and Comparing Different Euribor3M Forward Curves with Different Instrument Bootstrapping Sets
In this section, we build and compare different Euribor forward curves using different instrument bootstrapping sets. We define the instrument sets for each curve and build the forward curves using the dual curve approach. We then plot the forward curves to compare the results.

# Stability Comparison between Different Bootstrapping Sets
In this section, we apply predefined shifts to the data and rebuild the curves to analyze their stability. We use the tracking error and Tracking Error Volatility, expressed in basis points, to quantify the differences between the original and shifted curves. The subplots compare the original and shifted curves for each combination, and the statistical results provide a quantitative assessment of the stability.

# Usage
To use this repository, clone it to your local machine and ensure you have the necessary dependencies installed. Follow the steps in the Jupyter notebooks to load data, process it, and construct the curves.

# Contributing
Contributions are welcome! If you have any suggestions or improvements, please submit a pull request or open an issue.

# License
This project is licensed under the MIT License.

# Future Work
This study is still under development. The next steps include:

- Delving into and verifying the accuracy of incorporating the ECB liquidity check jump effect.
- Comparing different curves when varying the instruments used for bootstrapping.
- Further analysis and refinement of synthetic deposit construction methodologies.
- Overall correctness check
