# Módulo grafico

import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
import numpy as np

def fazer_graficos(X,y,salvar_figura=0,a=10,b=5):
    # X são os valores propriamente do gráfico, ex: df[i]
    # y é o rótulo, ex: 'i'
    if salvar_figura==0:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Tempo', fontsize=11)
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Tempo', fontsize=11)
        plt.savefig('{y}.png'.format(y=y))
        plt.show() 
          
def histograma(X,y,salvar_figura=0,a=10,b=5):
    # X são os valores propriamente do gráfico, ex: df[i]
    # y é o rótulo, ex: histograma de i
    if salvar_figura==0:
        plt.figure(figsize=(a,b)) 
        mu, std = norm.fit(X)
        plt.hist(X,density=True)
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        plt.plot(x, p, 'k', linewidth=2)
        plt.ylabel(y, fontsize=11)
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(a,b)) 
        mu, std = norm.fit(X)
        plt.hist(X,density=True)
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        plt.plot(x, p, 'k', linewidth=2)
        plt.ylabel(y, fontsize=11)
        plt.savefig('{y}.png'.format(y=y))
        plt.show()
        
def csd_parametric(X,y,salvar_figura=0,a=10,b=5):
    # X são os valores propriamente do gráfico, ex: df[i]
    # y é o rótulo, ex: 'i'
    if salvar_figura==0:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Tempo', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.mean() + 2*X.std(),color='g') 
        plt.axhline(X.mean() - 2*X.std(),color='g')  
        plt.ylim([-0.015, 0.12])
        plt.yticks([-0.01,0.00,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10,0.11])
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Tempo', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.mean() + 2*X.std(),color='g') 
        plt.axhline(X.mean() - 2*X.std(),color='g')  
        plt.ylim([-0.015, 0.12])
        plt.savefig('{y}.png'.format(y=y))
        plt.show()
        
def csd_non_parametric(X,y,salvar_figura=0,a=10,b=5):
    # X são os valores propriamente do gráfico, ex: df[i]
    # y é o rótulo, ex: 'i'
    if salvar_figura==0:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Tempo', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.quantile(0.95),color='g') 
        plt.axhline(X.quantile(0.05),color='g')  
        plt.ylim([-0.015, 0.12])
        plt.yticks([-0.01,0.00,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10,0.11])
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Tempo', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.quantile(0.95),color='g') 
        plt.axhline(X.quantile(0.05),color='g')  
        plt.ylim([-0.015, 0.12])
        plt.savefig('{y}.png'.format(y=y))
        plt.show()           
