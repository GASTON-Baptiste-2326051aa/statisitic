# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as p
import matplotlib.pyplot as plt

bd = p.read_csv("owid-covid-data-FRA-UK-US.csv")

#version sans lire l'énoncé
temp = bd.loc[(bd["date"]<'2021-06-01')&(bd["date"]>'2021-04-30')]
fra = temp.loc[temp["location"]=="France"]
usa = temp.loc[temp["location"]=="United States"]
uk = temp.loc[temp["location"]=="United Kingdom"]

print(temp["new_cases_smoothed_per_million"].mean())
print(fra["new_cases_smoothed_per_million"].mean())
print(usa["new_cases_smoothed_per_million"].mean())
print(uk["new_cases_smoothed_per_million"].mean())

#version group by ( + rapide )

fig, axs = plt.subplots(2, 2)


nc=temp.groupby("location")["new_cases_smoothed_per_million"]
moy_nc=nc.mean()
nd=temp.groupby("location")["new_deaths_smoothed_per_million"]
moy_nd=nd.mean()
ip=temp.groupby("location")["icu_patients_per_million"]
moy_ip=ip.mean()
hp=temp.groupby("location")["hosp_patients_per_million"]
moy_hp=hp.mean()
axs[0,0].pie(moy_nc,autopct=lambda z : str(round(z,2))+'%',pctdistance =0.6)
axs[0,1].pie(moy_nd,autopct=lambda z : str(round(z,2))+'%',pctdistance =0.6)
axs[1,0].pie(moy_ip,autopct=lambda z : str(round(z,2))+'%',pctdistance =0.6)
axs[1,1].pie(moy_hp,autopct=lambda z : str(round(z,2))+'%',pctdistance =0.6)





plt.show()


              


