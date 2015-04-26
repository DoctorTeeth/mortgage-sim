# This file defines the Bokeh applet
# The simulation logic is in simulator.py

from simulator import runSimulation
import logging

logging.basicConfig(level=logging.DEBUG)

from bokeh.plotting import figure
from bokeh.models import Plot, ColumnDataSource
from bokeh.properties import Instance
from bokeh.server.app import bokeh_app
from bokeh.server.utils.plugins import object_page
from bokeh.models.widgets import HBox, Slider, TextInput, VBoxForm


class SlidersApp(HBox):
    #An example of a browser-based, interactive plot with slider controls.

    extra_generated_classes = [["SlidersApp", "SlidersApp", "HBox"]]

    inputs = Instance(VBoxForm)

    text = Instance(TextInput)

    default_probability = Instance(Slider)
    prepay_probability = Instance(Slider)

    plot = Instance(Plot)
    source = Instance(ColumnDataSource)

    @classmethod
    def create(cls):
        """One-time creation of app's objects.

        This function is called once, and is responsible for
        creating all objects (plots, datasources, etc)
        """
        obj = cls()

        obj.source = ColumnDataSource(data=dict(x=[], y=[]))

        obj.text = TextInput(
            title="title", name='title', value='my sine wave'
        )

        obj.default_probability = Slider(
            title="default_probability", name='default_probability',
            value=0.01, start=0.0, end=1.0
        )
        obj.prepay_probability = Slider(
            title="prepay_probability", name='prepay_probability',
            value=0.02, start=0.0, end=1.0
        )

        toolset = "crosshair,pan,reset,resize,save,wheel_zoom"

        # Generate a figure container
        plot = figure(title_text_font_size="12pt",
                      plot_height=500,
                      plot_width=500,
                      tools=toolset,
                      x_axis_label="Months",
                      y_axis_label="$ (Millions)",
                      title="Cumulative Cash in Servicing Account",
                      x_range=[0, 120],
                      y_range=[0, 15000]

        )


        # Plot the line by the x,y values in the source property
        plot.line('x', 'y', source=obj.source,
                  line_width=3,
                  line_alpha=0.6
        )

        obj.plot = plot
        obj.update_data()

        obj.inputs = VBoxForm(
            children=[
                obj.default_probability, obj.prepay_probability
            ]
        )

        obj.children.append(obj.inputs)
        obj.children.append(obj.plot)

        return obj

    def setup_events(self):
        """Attaches the on_change event to the value property of the widget.

        The callback is set to the input_change method of this app.
        """
        super(SlidersApp, self).setup_events()
        if not self.text:
            return

        # Slider event registration
        for w in ["default_probability", "prepay_probability"]:
            getattr(self, w).on_change('value', self, 'input_change')

    def input_change(self, obj, attrname, old, new):
        """Executes whenever the input form changes.

        It is responsible for updating the plot, or anything else you want.

        Args:
            obj : the object that changed
            attrname : the attr that changed
            old : old value of attr
            new : new value of attr
        """
        self.update_data()

    def update_data(self):
        """Called each time that any watched property changes.
           We grab the parameters from the form and run the
           simulation in a 'pure' function
        """
        N = 120

        # Get the current slider values
        p = self.prepay_probability.value
        d = self.default_probability.value

        self.source.data = runSimulation(N,p,d)


# The following code adds a "/bokeh/sliders/" url to the bokeh-server. 
@bokeh_app.route("/bokeh/sliders/")
@object_page("sin")
def make_sliders():
    app = SlidersApp.create()
    return app
