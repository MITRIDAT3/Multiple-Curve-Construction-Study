
# Multiple Curve Construction Study


## Table of Contents
- Overview
- Data Loading
- Maturity Conversion and Evaluation Date
- €STR Discount Curve Construction
- Biased Euribor 6M Curve Construction
- Synthetic Deposits and Corrected Euribor Curve
- Single Curve Euribor Construction
- Forward Curve Comparison
- Usage
- Contributing
- License
- Future Work

## Overview

This study aims to construct multiple interest rate curves for €STR and Euribor using different sets of instruments.
The methodology follows the work by Ametrano and Bianchetti, implemented in Python with QuantLib.

## Data Loading

The data required for this study are stored in Excel files and include market quotes for OIS, deposits, FRA, and SWAP.
The data is processed to calculate the mid-rates from bid and ask prices.

## Maturity Conversion and Evaluation Date

The maturities are manually selected based on the study by Ametrano and Bianchetti.
These maturities are then converted into QuantLib periods, and the evaluation date is set for the curves.

## €STR Discount Curve Construction

The €STR discount curve is constructed using deposit rate helpers for short-term maturities and OIS rate helpers for longer maturities.
This allows for an accurate representation of the discount factors over a wide range of maturities.

## Biased Euribor 6M Curve Construction

The biased Euribor 6M curve is constructed using the first 6-month deposit as the initial pillar,
with additional FRA and SWAP rate helpers to extend the curve. The €STR curve serves as the discount curve in this approach.

## Synthetic Deposits and Corrected Euribor Curve

Synthetic deposit rate helpers are created by adjusting the forward rates derived from the €STR curve with a calculated spread (alpha).
These synthetic helpers, along with the original deposit, FRA, and SWAP helpers, are used to construct the corrected Euribor curve.

## Single Curve Euribor Construction

The single curve Euribor is constructed using SWAP rate helpers that discount using the implied Euribor curve.
This approach contrasts with the dual curve approach by utilizing the same curve for both discounting and forecasting.

## Forward Curve Comparison

The study concludes by comparing the forward Euribor curves generated by the dual curve and single curve approaches.
This comparison highlights the differences and provides insights into the effects of instrument selection on curve construction.

## Usage

To use this repository, clone it to your local machine and ensure you have the necessary dependencies installed.
Follow the steps in the Jupyter notebooks to load data, process it, and construct the curves.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License.

## Future Work

This study is still under development. The next steps include:

- Incorporating the turn-of-year jump effect.
- Considering ECB meeting dates for the construction of the €STR curve.
- Comparing different curves when varying the instruments used for bootstrapping.