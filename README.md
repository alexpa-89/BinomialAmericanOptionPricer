# Binomial American Option Pricer
Fast and straightforward implementation of the Cox-Ross-Rubinstein binomial option pricing model for American-style calls and puts.
Compatible with Python 3.7.

**1. Minimal dependencies**
   The function only requires a pre-installed Numpy library (no pandas, scipy etc.)

**2. Simple interface:**
   The  pricing model is implemented as a simple python function. No need to pre-install extensive libraries.
   Due to its simplicity, this option pricer can be readily integrated into your setup.
   
**3. Speed**
   The pricer is MUCH faster than many of the Python implementations of CRR I have seen on Github. 
   E.g. for a large number of steps (which is needed for more accurate pricing), the speed-up reaches a factor of ~20x compared to some existing implementations.

**4. Theta decay calculator (UPDATE Jan. 15th, 2025)**
Options lose value with passage of time, the process known as "theta decay". Roughly speaking, theta decay happens because the less time remains until the expiry date, the lower is the probability that the underlying will move _significantly_ in the direction beneficial for the option holder thus increasing the value of the option (as OTM and ATM options go ITM, and ITM options go deeper ITM). 
Thus, a theta decay calculator has been added to the **AmOption** module, allowing the user to see how the option value would change (as % of the initial value at time t0) over time, with the rest of the parameters remaining unchanged.

The calculator is implemented as the function **theta_decay(S0,K,T,sigma,r,Steps,OptType,val_periods, val_horizon)**.

The first 7 inputs that the **theta_decay** function takes are exactly the same as the ones passed to the **AmOption** function.

The 8th input (**val_periods**) determines in how many time steps the time until expiry at inception (**T**) is to be split (e.g. if T=1 year, than passing the value "365" as val_periods would produce a daily schedule of theta decay). **val_periods** MUST NOT be greater or equal to **Steps** (this will result in error and a termination of the function execution).

The 9th input (**val_horizon**) determines for how many steps ahead the theta decay is calculated. For example, one could choose **val_periods**=365 and **val_horizon**=91 to calculate _daily_ theta decay for the _next 3 months_. Setting **val_periods**=365 and **val_horizon**=365 will result in calculation of daily theta decay for the _full year_. Choosing val_horizon shorter than val_periods is especially practical if theta decay is calculated for higher frequencies, as the function **AmOption** needs to be executed n=val_horizon times. For example, calculating theta decay at _hourly_ frequencies for a _full year_ will result in 365*24=8760 **AmOption** function calls, which may take a significant amount of time. Simultaneously, it is unlikely that the rest of the parameters (e.g. **S0**, **sigma**, **r**) will remain unchanged for extended periods of time, making the calculation of theta_decay for the full year unnecessary.

_Dependencies_ 

**theta_decay** outputs a schedule of option values (as % of the initial value at t0) over the number of periods specified by val_horizon. In case you have matplotlib pre-installed, in addition to the array of values the function outputs a line plot of these values over time.

**DISCLAIMER**
Option values provided by the model DO NOT constitute an investment recommendation. The author of the implementation is in no way responsible for the investment outcomes that may result from using the pricer.
