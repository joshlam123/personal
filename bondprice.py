# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:35:51 2018

@author: Josh Lam
"""
import pandas as pd
link = 'https://www.bloomberg.com/markets/rates-bonds/government-bonds/us'

def read_data(link):
    data = pd.read_html(link)
    prices = data[0]
    return prices

def get_params(data):
    datas = []
    index = 0
    for i in range(len(data)):
        if str(i) in data[0].iloc[i]['Name']:
            index = i
    
    price = x[0].iloc[index]['Price']
    coupon = x[0].iloc[index]['Coupon']
    ytm = x[0].iloc[index]['Yield']
    duration = [float(x)*12 for x in x[0].iloc[1]['Name'].split()[i]][0]
    
    if duration not in [3,6,12]:
        duration *= 12
    return (price ,ytm, coupon, duration, freq)


def bond_price(par, ytm, coup, T, freq):
    freq = float(freq)
    periods = T*freq
    coupon = coup/100.0*par/freq
    dt = [(i+1)/freq for i in range(int(periods))]
    price = sum([coupon/(1+ytm/freq)**(freq*t) for t in dt]) + \
            par/(1+ytm/freq)**(freq*T)
    return price

def calculate_percentage_change(data):
	data_copy = data.copy()

	# Retrieve the close value column
	close = data_copy['close']
	
	# add a new column for percentage change
	data_copy['pct_chg'] = 0
	
	for i in range(0,len(close)-1):
		if i == len(close) - 1:
			data_copy.loc[i, 'pct_chg'] = 0
		else:
			data_copy.loc[i, 'pct_chg'] = (close[i + 1] - close[i]) / close[i] * 100
	return data_copy
	
def main():
	isEnd = False
	isExceptionFound = False
	while isEnd == False:
		try:
			if isExceptionFound == False:
                e all options for user selection
                epare_options()
                print(options)
			
			isExceptionFound = False
			
			# Append the question to prompt the user to enter their choice
			options_prompt = "Make your selection (E.g. if you want A, type 1):"
			
			# User makes their selection
			selected_option = input(options_prompt)
			
			# Retrieve the name of the selected option
			selected_option_name = retrieve_options(int(selected_option))
			
			# Retrieve data from the selected user option
			data = read_historical_data(selected_option_name)
           global link
            
           get_params(read_data(link))
           price = bond_price(par, ytm, coup, T, freq)
           
			
			# Generate percentage change
			data_perecentage_change = calculate_percentage_change(data)
			
			print(data_perecentage_change)
			
			# User makes their selection
			search_again = input('Do you want to search again? (Y/N)')
			
			if search_again != "Y" and search_again != "y":
				isEnd = True
		except InvalidOptionError as e:
			isExceptionFound = True
			print("Invalid Option detected! Please make your selection again:")
	
if __name__ == '__main__':
	main()