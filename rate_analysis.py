import pandas as pd

def analysis(days=32):
	df = pd.read_csv("data/hist_rates.csv")
	msgs = []
	nday = df.iloc[-days:,:]
	returns = nday.diff()
	hist_ret = returns.iloc[:-1,:]
	sd_ret = hist_ret.std(axis=0)
	today_ret = returns.iloc[-1,:]
	for i in range(len(returns.columns)):
		if (today_ret.iloc[i] >= sd_ret.iloc[i]*2) and (sd_ret.iloc[i] != 0):
			msg = str(hist_ret.columns[i])+"/USD rose 2 standard deviations above "+str(days-2)+" day average."
			msgs.append(msg)
		elif (today_ret.iloc[i] <= -sd_ret.iloc[i]*2) and (sd_ret.iloc[i] != 0):
			msg = str(hist_ret.columns[i])+"/USD dropped 2 standard deviations below "+str(days-2)+" day average."
			msgs.append(msg)

	if len(msgs) == 0:
		msgs.append("No rates exceeded 2 standard deviations today.")

	print("Analysis conducted...")
	return msgs
