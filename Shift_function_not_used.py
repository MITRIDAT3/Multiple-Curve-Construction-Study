ois_data = []
deposit_data = []
fra_data3M = []
forwards_ois_ecb_data = []  
swap_data3M = []
futures_data3M = []
settle_date = ql.Date(1, 1, 2020)






# Define Shifts and Pivot Dates
shift_start = -0.5  
shift_end = -0.1    

# Function to interpolate shifts smoothly between pivot dates
def smooth_interpolation(maturity_date, shift_start, shift_end, settle_date, last_date):
    total_days = (last_date - settle_date)
    days_to_maturity = (maturity_date - settle_date)
    shift = shift_start + (shift_end - shift_start) * (days_to_maturity / total_days)
    return shift

# Function to Apply Shocks to Data
def apply_shock(data, shift_start, shift_end, settle_date, last_date, is_futures=False):
    shifted_data = data.copy()
    for index, row in shifted_data.iterrows():
        maturity_date = row['Maturity_Date']
        shift = smooth_interpolation(maturity_date, shift_start, shift_end, settle_date, last_date)

        if is_futures:
            shifted_data.at[index, 'Mid_Rate'] -= shift
        else:
            shifted_data.at[index, 'Mid_Rate'] += shift
    return shifted_data


# Add Maturity Dates to Data
ois_data['Maturity_Date'] = ois_data['Period'].apply(lambda x: ql.TARGET().advance(settle_date, x))
deposit_data['Maturity_Date'] = deposit_data['Period'].apply(lambda x: ql.TARGET().advance(settle_date, x))
fra_data3M['Maturity_Date'] = fra_data3M['Start_Period'].apply(lambda x: ql.TARGET().advance(settle_date, x))
forwards_ois_ecb_data['Maturity_Date'] = forwards_ois_ecb_data['Start_Period']
swap_data3M['Maturity_Date'] = swap_data3M['Period'].apply(lambda x: ql.TARGET().advance(settle_date, x))
futures_data3M['Maturity_Date'] = futures_data3M['Start_Date']

# Get Last Maturity Date
all_maturities = pd.concat([
    ois_data['Maturity_Date'],
    deposit_data['Maturity_Date'],
    fra_data3M['Maturity_Date'],
    forwards_ois_ecb_data['Maturity_Date'],
    swap_data3M['Maturity_Date'],
    futures_data3M['Maturity_Date']
])
last_date = all_maturities.max()

# Apply Shocks to Data
s_ois_data = apply_shock(ois_data, shift_start, shift_end, settle_date, last_date)
s_deposit_data = apply_shock(deposit_data, shift_start, shift_end, settle_date, last_date)
s_fra_data3M = apply_shock(fra_data3M, shift_start, shift_end, settle_date, last_date)
s_forwards_ois_ecb_data = apply_shock(forwards_ois_ecb_data, shift_start, shift_end, settle_date, last_date)
s_swap_data3M = apply_shock(swap_data3M, shift_start, shift_end, settle_date, last_date)
s_futures_data3M = apply_shock(futures_data3M, shift_start, shift_end, settle_date, last_date, is_futures=True)
