# coding: utf-8
'''
"****************************************"
"* Universidad Nacional de Huancavelica *"
"*    Facultad Ciencias de Ingeniería   *"
"*         E.A.P Ingeniería Civil       *"
"****************************************"
"*Autor     : Vhb
"*Input     : Ingrese datos en el de altura y caudal observado
"*Output    : Gráfica y ecuación de curva gasto
'''

import matplotlib.pyplot as plt
import numpy as np
import math
import xlrd
plt.style.use('bmh')
def data():
    """ Load datos desde un excel"""
    xls = xlrd.open_workbook("Data.xlsx")
    libro = xls.sheet_by_index(0)
    Fil, Col = libro.nrows, libro.ncols
    H = np.asarray(libro.col_values(0, 1, Fil))
    Q = np.asarray(libro.col_values(1, 1, Fil))
    return H,Q
def regresionL(x,y):
    mean_x =np.mean(x)
    mean_y =np.mean(y)
    Ds_x = sum(x**2)/len(x) - mean_x**2 #np.std(x)
    Ds_y = sum (y**2)/len(y) - mean_y**2
    Ds_xy = sum(x*y)/ len(x) - mean_y*mean_x
    m = Ds_xy/Ds_x
    b = mean_y - m * mean_x
    r = Ds_xy / math.sqrt(Ds_x*Ds_y)
    r2 = r**2
    return (m,b,r2)

H,Q = data()[0],data()[1]
ho = 0.012
Lho = np.linspace(0.01,0.025,50)
ListR = []
ListK = []
Listn = []

for i in range(0,len(Lho)):
    ho = Lho[i]
    H_ho = H - ho
    LogH_ho = np.log10(H_ho)
    Log_Q = np.log10(Q)

    K = 10**(regresionL(LogH_ho, Log_Q))[1]
    n = (regresionL(LogH_ho, Log_Q))[0]
    Qca = K*(H - ho)**n

    r2 = (regresionL(Qca, Q)[-1])
    ListR.append(r2)
    ListK.append(K)
    Listn.append(n)
#print(ListR)
R_max = max(ListR)
Pos_opt = list(ListR).index(R_max)
print(Pos_opt)
h0_opt = Lho[Pos_opt]
print(h0_opt)
print(ListK[Pos_opt])
print(Listn[Pos_opt])
#GRafica Regresion de descennso
plt.plot(Lho,np.array(ListR)*10000,'go--', linewidth=1.5, label=u'$Gráfica\ r^{2}$')
plt.title(u"$Gráfica\ de\ Descenso$", fontsize=12)
plt.xlabel(u"$h0\ (mt)$")
plt.ylabel("$Coeficiente\ Determinación (r^{2})$")
plt.legend(loc="upper right", shadow=True, fontsize=10).get_frame().set_facecolor("lightsalmon")
plt.annotate(u"$Q =" + str(round(ListK[Pos_opt], 3)) + "(H-" + str(round(h0_opt, 6))+ ")" + "^{" + str(round(Listn[Pos_opt], 3))+ "}$" + "\n" + "$r^{2} =" +
             str(round(R_max, 7)) + " $", xy=(h0_opt*0.5, np.mean(R_max) * 10000),
           xycoords='data',
          va="center", ha="left", bbox=dict(boxstyle="round, pad=0.5", fc="0.65"))
#u"            $Curva\ Gasto$"+ "\n" + "\n" +"$H_{0} =" + str(round(h0_opt, 5)) + " mt\ $"
plt.grid(True)
plt.savefig("D:\\Cursos FIC\\Ingenieria Civil UNH\\Tesis FIC\\FIC\\Tesis_VictorB\\Documentacion\\Latex\\Tesis_Tex\\Imagenes_Tesis\\Cap_03\\DescensoError.png",dpi=400)
plt.autoscale(tight=True)
plt.margins(0.1)
plt.show()

#GRafica Caudal
plt.plot(np.sort(Q), np.sort(H), 'ko--', linewidth=1.5, label=u'$Caudal\ m^{3}/seg$')
plt.title(u"$Gráfica\ de\ Altura\ vs\ Caudales$", fontsize=12)
plt.xlabel(u"$Caudal\ (m^{3}/seg)$")
plt.ylabel("$Altura\ (m)$")

plt.legend(loc="upper left", shadow=True, fontsize=10).get_frame().set_facecolor("lightsalmon")

for j in range (0,len(Q)):
    plt.annotate(u"$Q_{0} =" + str(round(np.sort(Q)[j], 2)) + "$", xy=(np.sort(Q)[j]*1.025, np.sort(H)[j]),
              xycoords='data',
            va="center", ha="left") #, bbox=dict(boxstyle="round, pad=0.5", fc="0.65"
plt.grid(True)
plt.savefig("D:\\Cursos FIC\\Ingenieria Civil UNH\\Tesis FIC\\FIC\\Tesis_VictorB\\Documentacion\\Latex\\Tesis_Tex\\Imagenes_Tesis\\Cap_03\\Caudales.png",dpi=400)
plt.autoscale(tight=True)
plt.margins(0.1)
plt.show()

#list(self.Duracion).index(60)
#res = regresionL(H,Q)
#print(res)


