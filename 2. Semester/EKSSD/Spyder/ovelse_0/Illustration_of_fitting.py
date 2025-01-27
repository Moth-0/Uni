# %% load libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sc
 
# %% clean up
plt.close('all')
 
# %% Define fitting functions 
 
# a simple way of writing the function
#def func_fit(x, *p):                        
#    return a*np.sin(2*np.pi*b*x + c) + d    
 
 
# a smart way of writing the fit function
def func_fit(x, *p):                        # NB using the '*args', here given as *p
    a=p[0]                                  # is a way to give a varaible input                               # and still use basically the same script
    return a*x
 
 
# %% Making as set of sample data
 
# define data
x_data = [0, 10, 20, 30, 40, 50]

y_data = [1.734, 1.444, 1.178, 0.9178, 0.6519, 0.3813]
mu    = 0;                                                  # for adding noise
sigma = 0.1;                                                # for adding noise
noise_on_data = np.random.normal(mu,sigma, len(y_data));    # errors
y_data=y_data + noise_on_data;                              # y_data with noise
 
ey_data = y_data*0+sigma;                                   # error on y_data
 
# %% Plot data together with the initial guess
 
# inital guess
a_guess = 9                                  #
b_guess = 0.11                               # NB- for fitting a sine the guess is rather important !
c_guess = 0                                  # try for example to set b=0.5 and see the fit
d_guess = 2
p_init = [a_guess, b_guess, c_guess, d_guess];
 
y_guess = func_fit(x_data, *p_init)          # make a array with the guess function
 
 
 
# make figure with data and the guess function
fig = plt.figure(1)                            # makes a figure; fig is a handle to the figure
fig.clf()                                      # clear the figure
fig.set_size_inches(6,5,forward=True)          # sets the image size (w,h) in inches (1inch = 2.54 cm)
plt.rc('xtick',labelsize=14)                   # rc ~ "Run and Configure" # set size of axis-numbers#
plt.rc('ytick',labelsize=14)                   # set the size of the axis-numbers
    
# Plot of initial data and guess function  
ax = fig.add_subplot(1,1,1)                                # makes a subplot; ax is the handle to the axes #
ax.set_title('An example of a fit with curve_fit')
                                                           # NB use \ to continue command on the next line#
h1  = ax.errorbar(x_data, y_data, yerr=ey_data, xerr=None,label='data',\
                 fmt='.',color='k', marker='.',\
                 uplims=False, lolims=False, capsize=3,\
                 elinewidth=1,markeredgewidth=1)           # plotting with errorbars
 
 
h2  = ax.plot(x_data, y_guess,label='Initial guess',\
              color='b', marker=None,\
              linewidth=1)                               # plotting the guess function
 
 
ax.set_xlabel(r'x data [unit]',fontsize=14)                  # set the label on the x-axis
ax.set_ylabel(r'y data [unit]',fontsize=14)             # set the label on the y-axis
    
#ax.set_xlim(0,10)                                       # set the limit on the x-axis
ax.set_ylim(-15,20)                                       # set the limit on the y-axis
 
 
ax.set_xscale('linear')                                     # 'linear' or 'log'
ax.set_yscale('linear')                                     # 'linear' or 'log'
 
#ax.set_xticks(np.array([0, 25, 50, 75, 100, 125]))          # set certain xtick - not always needed
#ax.set_yticks(np.array([0, 50, 100, 150, 200, 250]))        # set certain yticks - not always needed
 
 
ax.set_frame_on(True)     
ax.legend(loc='upper left',frameon=False)
 
 
 
# %% Doing the fitting
p_opt, pcov = sc.curve_fit(func_fit, x_data, y_data, sigma=ey_data,\
                       absolute_sigma=True,\
                       p0=p_init)                                        # doing the fit
                                                                         # parameters returned in p_opt
e_p_opt = np.sqrt(np.diag(pcov))                                         # errorbars as square root of diagonal elements
                                                                         # in the covariance matrix
 
chi_square = np.sum(((y_data-func_fit(x_data, *p_opt))/ey_data)**2)      # caluculate chi^2 for the fit
 
y_fit =func_fit(x_data,*p_opt)                                          # array with the fitted function
 
 
 
# adding the fit to the plot
ax.plot(x_data,y_fit,'-r',label='fitted curve' )
ax.legend()
ax.legend(loc='upper left',frameon=False)
 
 
# summarize the fit in some text lines
num_dig = 3
line1 = '############# Fit result ######################'
line2 = 'a = ' + str(round(p_opt[0],num_dig)) + ' $\pm$ ' + str(round(e_p_opt[0],num_dig))
line3 = 'b = ' + str(round(p_opt[1],num_dig)) + ' $\pm$ ' + str(round(e_p_opt[1],num_dig))
line4 = 'c = ' + str(round(p_opt[2],num_dig)) + ' $\pm$ ' + str(round(e_p_opt[2],num_dig))
line5 = 'd = ' + str(round(p_opt[3],num_dig)) + ' $\pm$ ' + str(round(e_p_opt[3],num_dig))
line6 = '$\chi^2$ = ' + str(round(chi_square,2))
line7 = '###############################################'
 
ax.text(8,12,line2 + '\n' + line3 +\
        '\n' + line4 + '\n' + line5 +'\n' + line6)                      # NB - simple way of adding string
plt.show()
 
 
# print the fitted values to the console
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)                                                  
 
# save figure
figure_name = 'test_figure_fit.png';                            
fig.savefig(figure_name)