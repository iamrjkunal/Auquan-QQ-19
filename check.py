import pandas as pd
import numpy as np
import os.path
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
    
    
    
    
#### LOAD THE HELPER FUNCTIONS BELOW####
#### IMPORTANT: DONOT change these functions or your final submission will not evaluate correctly###

## This downloads your datafile, Do not change this function
def downloadFile(dataSetId):
      fileName = '%s.csv' % (dataSetId)
      url = 'https://raw.githubusercontent.com/Auquan/qq-winter2019/master/' + fileName

      response = urlopen(url)
      status = response.getcode()
      if status == 200:
          print('Downloading the dataset %s' % (fileName))
          with open(fileName, 'w') as f:
              f.write(response.read().decode('utf8'))
          return True
      else:
          logError('File not found. Please ensure you are working with correct data set Id')
          return False


        
## This calculates the reward, Do not change this function
def getReward(wt, wt_1, ri, l, k):
    ri.fillna(0, inplace=True)
    returns = np.dot(wt_1, ri)
    port_returns.append(returns)
    volatility = np.std(port_returns) #np.sqrt(np.dot(weights.T, np.dot(cov_annual, weights)))
    sharpe = np.sum(port_returns) / volatility
    sharpe_ratio.append(sharpe)
    port_volatility.append(volatility)
    phi = k*(wt - wt_1).abs().sum()
    reward = returns - l*volatility - phi
    print(returns, volatility, phi, sharpe, reward)
    return reward



## Do not change this function, this verifies if all constraints are met
def checkConstraints(wt, wt_1, wi, Dt, St, Qt, g, U, t, T, P, delta, chi, eta):
    violated = False
    if wt.sum()!=1:
        print("Fully Invested Constraint Violated: Sum of weights is not 1")
        violated = True
    if (wt>g).any():
        print("Diversification Constraint Violated: All weights are not less than parameter g")
        violated = True
    turnover_list.append((wt - wt_1).abs().sum())
    if (np.sum(turnover_list[-12:])>U):
        print("%0.2f Turnover Constraint Violated: Turnover Limit exceeded"%((wt - wt_1).abs().sum()))
        violated = True
    if (wt<t).any():
        print("Shortsell Constraint Violated: all weights are not greater than parameter t")
        violated = True
    if wt[wt<0].sum()<T:
        print("Max Shortsell Constraint Violated: sum of all weights are not greater than parameter T")
        violated = True
    if wt[wt!=0].count() < P:
        print("Min number of positions Constraint Violated: count of all weights <>0 are not greater than parameter P")
        violated = True
    if (wt*Dt).sum()/ (wi*Dt).sum() > delta:
        print("Duration Constraint Violated: wt*Dt/ wi*Dt is greater than parameter delta")
        violated = True
    if (wt*St).sum()/ (wi*St).sum() > chi:
        print("Spread Constraint Violated: wt*St/ wi*St is greater than parameter chi")
        violated = True
    if (wt*(1-Qt)).sum() != 0:
        print("Qualification Constraint Violated: wt*(1-qt) is not zero")
        violated = True
#     if returns - Rlow/ volatility <= np.sqrt(1-eta):
#         print("Max Risk probability Constraint Violated: returns - Rlow/ volatility <= np.sqrt(1-eta)")
#         violated = True
            
    return violated
        


## Do not change this function, this verifies if final constraints are met
def checkFinalConstraints(Rmin, volmax):
    violated = False
    if np.sum(port_returns)<Rmin:
        print("Total Return Constraint Violated: Total Return is less than Index Return")
        violated = True
    if port_volatility[-1]>volmax:
        print("Volatility Constraint Violated: Vol is higher than Index Vol")
        violated = True
    if sharpe_ratio[-1]<Rmin/volmax:
        print("Sharpe Ratio Constraint Violated: SR is less than Index SR")
        violated = True
        return violated


#### FILL THE FUNCTIONS BELOW ####

## Step 1: Fill the asset group you want to model for
## This can be 'G1' or 'G2'
def getSymbolsToTrade():
    ################################################
    ####   COPY FROM BELOW INTO TEMPLATE FILE   ####
    ################################################
    
    return 'G1'


## Step 2: Fill the logic to generate weights

## This function takes in the following inputs:
## identifiers: asset identifiers
## reward: reward at time t (based on w(t-1))
## wi: weights to initialize from, if you want to use
## Dt: value of column 'd' per asset
## St: value of column 'S' per asset
## Qt: value of column 'q' per asset
## g: value of constant gamma, read problem descrption for details
## U: value of constant U, read problem descrption for details
## t: value of constant t, read problem descrption for details
## T: value of constant T, read problem descrption for details
## P: value of constant P, read problem descrption for details
## delta: value of constant delta, read problem descrption for details
## chi: value of constant chi, read problem descrption for details
## eta: value of constant eta, read problem descrption for details
## **kwargs: any additional params you want to add can be specified here. kwargs is a dictionary

### do not change the inputs to the function. If you want any extra inputs, specify them in **kwargs
### you can lookup this tutorial on how to use **kwargs https://www.geeksforgeeks.org/args-kwargs-python/

def getWeights(identifiers, reward, wi, Dt, St, Qt, g, U, t, T, P, delta, chi, eta, **kwargs):
    ################################################
    ####   COPY FROM BELOW INTO TEMPLATE FILE   ####
    ################################################
    # call getprediction() we get r(t+1) and use it with call getreward() recursively to optimize w(t)  
    # weights = w(t)
    #weights = pd.Series(np.random.random(len(identifiers)), index=identifiers)
    
    weights[Qt==0] = 0
    weights = weights/weights.sum()
    if (weights>g).any():
        weights[weights>g] = g
        weights = weights/weights.sum()
    return weights
    


## Step 3: Optional: Fill in the logic to return predictions for return on asset
## This function takes in the same inputs as getWeights()

### do not change the inputs to the function. If you want any extra inputs, specify them in **kwargs
### you can lookup this tutorial on how to use **kwargs https://www.geeksforgeeks.org/args-kwargs-python/

def getPrediction(identifiers, wi, Dt, St, Qt, g, U, t, T, P, delta, chi, eta, **kwargs):
    ################################################
    ####   COPY FROM BELOW INTO TEMPLATE FILE   ####
    ################################################
    # call  LSTM function for each assets to predict each r(t+1) 
    return np.zeros(len(identifiers))



## Step 4: Optional: If your code uses any other helper functions, fill them here

### again do not change the inputs to the function. If you want any extra inputs, specify them in **kwargs
### you can lookup this tutorial on how to use **kwargs https://www.geeksforgeeks.org/args-kwargs-python/
class CustomFeatures():

    def newFeature1(self, **kwargs):
    ################################################
    ####   COPY FROM BELOW INTO TEMPLATE FILE   ####
    ################################################
    ##implement LSTM
    
        return None


## This loads asset data and lets you explore the dataset
## Make sure the worksheet and data are in the same folder

index = getSymbolsToTrade()
if not os.path.isfile('%s.csv'%index):
    downloadFile(index)
idx_data = pd.read_csv('%s.csv'%index, index_col='TimeStamp')
idx_data.sort_index(axis=0, level=None, ascending=True, inplace=True)
print("Data Column Names:")
print(idx_data.columns)
print(index, idx_data.index[0], idx_data.index[-1])
print(idx_data.head(10))


## DONOT CHANGE ANYTHING BELOW THIS

# empty lists to store returns, volatility and weights of imaginary portfolios
port_returns = []
port_volatility = []
sharpe_ratio = []
asset_weights = []
reward_list = []
turnover_list = []
idx_returns = []





### Evaluator to getweights at everytime t and calcuate reward + check if constraints are met

## specifying all the constants
counter = 0
l = 0.1
k = 0.03
g = 0.03
U = 2.5
t= 0
T = 0
P = 80
delta = 0.5
chi = 0.1
eta = 0.95

## initializing arrays
dates = idx_data.index.unique()
port_returns.append(0)
port_volatility.append(0)
sharpe_ratio.append(0)
asset_weights.append(pd.Series(idx_data[idx_data.index == dates[0]]['wI'].values/100, 
                               index=idx_data[idx_data.index == dates[0]]['Identifier'].values))
reward_list.append(0)
idx_returns.append(0)
turnover_list.append(0)
## looping over all dates
while counter < len(dates):
    date = dates[counter]
    
    ## load all the data for a date
    date_data = idx_data[idx_data.index == date]
    
    ## get all the identifiers for a date
    cusips = date_data['Identifier'].unique()
    date_data.set_index( date_data['Identifier'], inplace=True)
    #load specific feature info
    wi = pd.Series(date_data['wI']/100, index = date_data['Identifier'])
    Dt = pd.Series(date_data['d'], index = date_data['Identifier'])
    St = pd.Series(date_data['S'], index = date_data['Identifier'])
    qt = pd.Series(date_data['q'], index = date_data['Identifier'])
    
    ## old weights
    wt_1 = asset_weights[-1]
    
    ri = pd.Series(date_data['TRR'], index = wt_1.index)
    
    ## get new weights
    wt = getWeights(cusips, reward_list[-1], wi, Dt, St, qt, g, U, t, T, P, delta, chi, eta)
    
    ## calculate reward
    reward = getReward(wt, wt_1, ri, l, k)
    
    ## store relevant info in their lists
    asset_weights.append(wt)
    reward_list.append(reward)
    counter += 1
    idx_returns.append(np.dot(wi, pd.Series(date_data['TRR'], index = wi.index)))

    ## verify if all constraints are met
    if checkConstraints(wt, wt_1, wi, Dt, St, qt, g, U, t, T, P, delta, chi, eta):
        print("ERROR!!!! weights don't meet contraints, exiting")
        break

## check if contraints on total return and risk are met        
Rmin = np.sum(idx_returns)
volmax = np.std(idx_returns)
if checkFinalConstraints(Rmin, volmax):
    print("ERROR!!!! weights don't meet return/risk limit contraints, exiting")
else:
    print("Portfolio Metrics:")
    print("Total Return: %.2f"%np.sum(port_returns))
    print("Standard Deviation: %.2f"%port_volatility[-1])
    print("Sharpe Ratio: %.2f"%sharpe_ratio[-1])
    
