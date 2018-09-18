# to use a function in the program the funcion inside the program needs to have the same name as the file

def lotka_volterra(t,x,c):
    
    # define the initial values
    g=x[0];
    r=x[1];
    f=x[2];

    size=c[0]
    
    alpha=c[1]
    beta_gr=c[2]
    beta_r=c[3]
    gamma_r=c[4]
    gamma_f=c[5]
    delta_r=c[6]
    delta_f=c[7]    
    k_g=np.power(size,c[8])
    k_r=np.power(size,c[9]);
    s_f=c[10]
    s_r=c[11]
    

    dg=(alpha*(1-g/k_g)-beta_gr*(r/(k_g+g)))*g;
    dr=(gamma_r*(g/(k_g+g-s_r))-beta_r*(f/(k_r+r))-delta_r)*r;
    df=(gamma_f*r/(k_r+r-s_f)-delta_f)*f;
    
    return [dg, dr, df]
