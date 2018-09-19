# Disease_modeling
Disease models

This a simple program for disease spreading modeling. The original purpose of this program was to test different ODE systems which intended to model the spread of diseases using different computational solver methods. Some other features were added after. The program was written in python and it is presented in a form of a GUI, the project was developed using the PyQt4 GUI toolkit. The program was tested using **Python2** the implementation using python 3 wasn't tested.  

To start the program you just need to run **main.py**

The program by default has the options 
+ Forward Euler method
+ Runge Kutta 2nd order 
+ Runge Kutta 4th order

and the disease spreading models used were>

+ SIS Model *, **
+ SIR Model *  

Between the extra features added is the option of select your own solver method and ODE model so be solved, but it needs to be improved and still has some flaws. 

*[Shabbir et al, A note on Exact solution of SIR and SIS epidemic models](https://arxiv.org/pdf/1012.5035.pdf) 

**[Towers et al, Pandemic H1N1 influenza: predicting the course of a pandemic and assessing the efficacy of the planned vaccination programme in the United States ](https://www.eurosurveillance.org/content/10.2807/ese.14.41.19358-en)

