# Import libraries:

import numpy as np # NumPy for maths operations.
import re # Regular expressions - Used for converting input string to maths function.
import matplotlib.pyplot as plotter # MatplotLib & PyPlot for plotting graph.
import matplotlib # Import the rest of MatPlotLib.

# Set-up dictionary to convert to functions from string input:

replacement_words = {"sin":"np.sin","cos":"np.cos","exp":"np.exp","sqrt":"np.sqrt","^":"**","ln":"np.log"}

# Set-up whitelist array of allowed inputs:

input_words = ["x","sin","cos","sqrt","exp","ln"]

# Function to convert string to function of x.

def stringToFunc(string):
    for word in re.findall('[a-zA-Z_]+', string): # Find all of the words and check if whitelisted (in input_words array).
        if word not in input_words:
            print("'{}' is not allowed in expression".format(word))

    for old, new in replacement_words.items():
        string = string.replace(old, new)

    def func(x):
        return eval(string)

    return func

inputFunc = input("Enter Function: f(x) = ")
func = stringToFunc(inputFunc) # Use 'stringToFunc' function to convert input string to function.

lowerLim_X = int(input("Enter lower limit for x: "))
upperLim_X = int(input("Enter upper limit for x: "))
lowerLim_Y = int(input("Enter lower limit for y: "))
upperLim_Y = int(input("Enter upper limit for y: "))

x = np.arange(lowerLim_X - 10, upperLim_X + 10, 0.01) # Fill array with values between x limits in 0.01 increment (to be used to get y = f(x) at these points)
# (Range is extended by 10 in each direction to account for scaling and scrolling etc.)

y = func(x) # Create array of y-value calculated from function f(X) = 'func' for every value in 'x' array.

# Set up matplotlib font:

plotter_font = {"family":"sans", "weight":"normal", "size":9} # Define font for use with matplotlib.
matplotlib.rc("font", **plotter_font) # Tell matplotlib to use 'plotter_font' font.

windowFigure = plotter.figure() # Set window title.
windowFigure.canvas.set_window_title('Fin Warman - MatPlotLib Function Plotter') 

# Use MatPlotLib to graph x and y=f(x):
plotter.plot(x, y, "-k", lw=1)

# Set axes so that are centred on the origin:

ax = plotter.subplot(111)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.set_xlim([lowerLim_X,upperLim_X])
ax.set_ylim([lowerLim_Y,upperLim_Y])
ax.set_title(str("f(x) = " + inputFunc))


# Show the graph in the GUI window.
plotter.show()
