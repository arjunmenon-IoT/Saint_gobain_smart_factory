Gas_concentration = lambda mill,filter : 651.1 + 30.71*mill +  2.672*filter + -70.33*pow(mill, 2) + 2.11*mill*filter + 2.739*pow(filter, 2) + 95.94*pow(mill, 3) + 0.9131*pow(mill, 2)*filter + -3.306*mill*pow(filter, 2) + -1.954*pow(filter,3) + -51.9*pow(mill,4) + -0.272*pow(mill,3)*filter + -0.2167*pow(mill,2)*pow(filter,2)  + 1.783*mill*pow(filter,3) + 0.5365*pow(filter,4) + 9.493 *pow(mill,5) + -0.1104 *pow(mill,4)*filter + 0.2851*pow(mill,3)*pow(filter,2) + -0.1511*pow(mill,2)*pow(filter,3) +  -0.3027 *mill*pow(filter,4) + -0.04373 *pow(filter,5)
Mill_humidity = lambda mill,filter : 330.9  + -65.39*mill + -28.82*filter + 19.78*pow(mill,2) + 16.17*mill*filter + -4.967*pow(filter,2) +  -8.268*pow(mill,3) +  -5.342*pow(mill,2)*filter + -4.967*mill*pow(filter,2) +  11.71*pow(filter,3) + 2.198*pow(mill,4) + 1.67*pow(mill,3)*filter + 0.8435*pow(mill,2)*pow(filter,2)  +  2.649*mill*pow(filter,3) +  -6.056*pow(filter,4) + -0.2222*pow(mill,5) + -0.2476*pow(mill,4)*filter + -0.04233*pow(mill,3)*pow(filter,2) + -0.1799*pow(mill,2)*pow(filter,3) +  -0.4*mill*pow(filter,4) + 1.022*pow(filter,5)
Recirc_hum = 335.3 + 176.3*mill + -66.03*filter + -565.4 *pow(mill,2) + -15.08*mill*filter + 18.04*pow(filter,2) + 501.4*pow(mill,3) + 61.3*pow(mill,2)*filter + -5.195*mill*pow(filter,2) + -7.313*pow(filter,3) + -188.7*pow(mill,4) + -34.89*pow(mill,3)*filter + -1.721*pow(mill,2)*pow(filter,2) + 2.293*mill*pow(filter,3) + 2.071*pow(filter,4) + 25.87*pow(mill,5) + 6.019*pow(mill,4)*filter + .7778*pow(mill,3)*pow(filter,2) + -0.2169*pow(mill,2)*pow(filter,3) + -0.3238*mill*pow(filter,4) + -0.2222*pow(filter,5)