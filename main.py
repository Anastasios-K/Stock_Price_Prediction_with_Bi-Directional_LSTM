from scr.preproc import read_data, add_nans, detect_nan_values, detect_null_values


url_list = ["data", "btcusd_datetime.csv"]

df = read_data(url_list=url_list)
df_nan = add_nans(df=df)

x = detect_nan_values(df_nan)
y = detect_null_values(df_nan)
