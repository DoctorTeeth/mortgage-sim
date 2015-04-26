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

