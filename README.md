Mortgage Simulator
=================

This Bokeh applet generates an interactive graph with sliders.

The graph shows the cumulative amount of cash in a 
mortgage servicer account for a group of simulated mortgages.

Adjusting the sliders will change the probability that any given mortgage
will prepay or default in any given month.

Running
=======

Assuming that you have the latest version of bokeh-server intalled, 
execute the following in the root directory:

    bokeh-server --script sliders_app.py
    
Then navigate to the following URL:
    
    http://localhost:5006/bokeh/sliders

Simulation Details
==================

For this simulation, we use a pool of 100 mortgages
with a 4% fixed interest rate and $100,000 initial principal.

The simulation runs for 120 months (10 years).

Every month, all of the active loans have some chance P of 
prepaying and some chance D of defaulting, as specified by the sliders.
The values of D and P both lie in the interval [0,1]. 
If the simulator wants a loan to both default and prepay, 
it "flips a coin" to determine which will happen.

Loans that default are assumed to generate 80% of their remaining
principal in value. 

Loans that prepay are assumed to generate 100% of
their remaining principal in value.

Everything else about the simulation is heavily simplified:
Defaults generate revenue immediately, default and prepay rates
are independent across the pool, there are no servicing fees, etc.

Miscellaneous
=============

The results of the simulation are close to what we would expect.

With the prepay and default rates set to 0, the graph is a straight line, 
since the same payment is received for each of the loans every month.

With the default rate set to 1 and the prepay rate set to 0, 
the cash recovered remains the same after the first month, 
and the amount is equal to 80% of the total initial principal.

With a prepay rate of 1 and a default rate of 0, 
the servicer simply recovers all the principal immediately and 
receives no interest.

With both rates set to 1, the total cash recovered by the servicer is
around 90% of the initial total principal, or halfway between the above two 
scenarios. This makes sense - based on the way the simulation works, 
half of all loans will prepay and half of all loans will default, all in 
the first month.

You can play around with the applet yourself to see what the graph 
looks like in less extreme scenarios.
