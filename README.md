# BinomialAmericanOptionPricer
Fast and straightforward implementation of the Cox-Ross-Rubinstein binomial option pricing model for American-style calls and puts.

**1. Minimal dependencies**
   The function only requires a pre-installed Numpy library (no pandas, scipy etc.)

**2. Simple interface:**
   The  pricing model is implemented as a simple python function. No need to pre-install extensive libraries.
   Due to its simplicity, this option pricer can be readily integrated into your setup.
   
**3. Speed**
   The pricer is MUCH faster than many of the Python implementations of CRR I have seen on Github. 
   E.g. for a large number of steps (which is needed for more accurate pricing), the speed-up reaches a factor of ~20x compared to some existing implementations.
