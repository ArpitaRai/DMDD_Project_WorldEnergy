import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly_express as px

#CO2EmissionData Representation
#----------------------------------------------------------------------------------------------------------------------------------------------
df = pd.read_excel('CO2Emission.xlsx', sheet_name='Sheet1')
df = df.dropna() 

x = df.iloc[0:27, 0]
y = df.iloc[0:27, 1]

# Add labels
plt.xlabel('CO2Emission FY-2021')
plt.ylabel('Countries')
plt.title(' C02 Emission of top 15 Countries (In Million Tonnes)')

# Create the plot
plt.barh(x,y, color = ['red'])

# Show the plot
plt.show()

#RenewableEnergyGeneration Representation
#----------------------------------------------------------------------------------------------------------------------------------------------
df = pd.read_excel('RenewableEnergyGeneration.xlsx', sheet_name='Sheet1')
df = df.dropna() 

x = df.iloc[0:27, 0]
y = df.iloc[0:27, 1]

# Add labels
plt.xlabel('Renewable Energy Production FY-2021')
plt.ylabel('Countries')
plt.title('Renewable Energy Geneartors (In Terawatt-hours)')

# Create the plot
plt.barh(x,y, color = ['green'])

# Show the plot
plt.show()

#RenewableenergyConsumption
#----------------------------------------------------------------------------------------------------------------------------------------------

df = pd.read_excel('RenewableenergyConsumption.xlsx', sheet_name='Sheet1')
df = df.dropna() 

x = df.iloc[0:27, 4]
y = df.iloc[0:27, 5]

# Add labels
plt.xlabel('Renewable Energy Consumption FY-2021')
plt.ylabel('Type of Renewable Energy')
plt.title('Renewable Energy Consumption (In Terawatt-hours)')

# Create the plot
plt.barh(x,y, color = ['blue'])

# Show the plot
plt.show()


#----------------------------------------------------------------------------------------------------------------------------------------------

y = np.array([3, 2.80,6.101,35,34,10])
mylabels = ["WindEnergy", "SolarEnergy", "Geo-BioMass" , "Oil", "Gas", "Coal"]

plt.title('Energy Consumption Percentage in USA')
plt.pie(y, labels = mylabels)
plt.show() 