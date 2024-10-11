import numpy as np
import matplotlib.pyplot as plt

def buildLinearPlot(x, y, xname, yname):
    # Example data: two arrays with equal elements
    x = np.array(x)
    y = np.array(y)

    # Scatter plot of the points
    plt.scatter(x, y, color='blue', label='Data points')

    # Fit a straight line through the points (1st degree polynomial)
    coefficients = np.polyfit(x, y, 1)
    slope, intercept = coefficients

    # Generate y-values based on the fitted line
    y_fit = slope * x + intercept

    print(-intercept/slope)

    # Plot the fitted line
    plt.plot(x, y_fit, color='red')

    plt.axhline(y=0, color='green', linestyle='--', 
                label=f'$\\text{{U}}_3 = 0$')

    # Add labels and title
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.legend()

    # Adjust the axis limits to zoom out
    x_padding = (max(x) - min(x)) * 0.5  # 10% padding
    y_padding = (max(y) - min(y)) * 0.5  # 10% padding
    plt.xlim([min(x) - x_padding, max(x) + x_padding])
    plt.ylim([min(y) - y_padding, max(y) + y_padding])

    # Show the plot
    plt.show()

NRY = {'U': 0.6, 'NU': 5.5 * 10**14}
NRB = {'U': 0.9, 'NU': 9.6 * 10**14}
NRW = {'U': 5.2, 'NU': 11.8 * 10**14}

U_NU = [NRY, NRB, NRW]

Udata  = [el['U']  for el in U_NU]
NUdata = [el['NU'] for el in U_NU]

print(Udata[::-1])
print(NUdata[::-1])

buildLinearPlot(NUdata, Udata, '$\\nu$', '$\\text{U}_\\text{Z}$')
# buildLinearPlot(Udata, NUdata, f'U', f'NU')