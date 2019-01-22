# qq-winter2019
Data, Worksheet and template file for winter 2019 qq

## Instructions :
* Download the jupyter notebook Worksheet.ipynb and file `problem1_template.py`.
* If you are new to jupyter, please follow detailed instructions on how to set it up and run the notebook here: https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/install.html
* First solve the problem in jupyter notebook Worksheet.ipynb. The worksheet contains helper functions to guide you.
* Specify the asset group that you are modeling for in function `getSymbolsToTrade()`
* The bulk of your code will go in the function `getWeights()` where you will fill the logic to assign weights to each asset in that group.
* If you wish, depending on the approach you are taking, you can also use the function `getPrediction()` which call all of these features at time t and combine them in a meaningful way to predict rt+1,i and σt+1,i for each asset in that group. You can then use this prediction to allocate weights wt,i so that predicted Reward, Rt+1, i is maximized - this is only a suggested approach, you don’t have to follow this.
* If you run the worksheet, it will evaluate your logic, calculate reward for each timestep and also verify that your weights meet all the constraints at all times.
* Once you are satisfied, copy your function body into problem1_template.py for the following functions:
  * `getSymbolsToTrade()`
  * `getWeights()`
  * `getPrediction()`
  * `Any new feature you have created`
* DO NOT change any other function except these three in the file or your submission will not evaluate correctly. If you are confused about where to make changes, search for TODO comments in the file.
* You only need to submit `problem1_template.py` on the platform
* Your function’s final output should be a weight vector, wt, whose ith element, wt,i, is the proportion of asset i in the group at time t. The elements of wt always sum up to one by definition, Σ wt,i = 1, ∀t.
* The toolbox will run this function for all datasets at all times to get weights for every asset at all times t. Based on the weights at time t, the toolbox will calculate the reward R at time t+1
* At any given time t, your model should only use data from time T=0 to T=t. Our toolbox is designed to prevent you from accessing data beyond the timestamp for which you are predicting.
* Additionally, your code should provide this output for every timestamp, and our toolbox will provide a score for each timestamp. You can use this score for reinforcement-style learning.

