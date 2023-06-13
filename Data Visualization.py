#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

display(data.head(10))


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.scatter(data['Month'], data['Quantity'])

plt.title("Scatter Plot")

plt.xlabel('Month')
plt.ylabel('Quantity')

plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')

plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.plot(data['Month'])
plt.plot(data['Quantity'])

plt.title("Line Chart")

plt.xlabel('Month')
plt.ylabel('Quantity')

plt.savefig('line.png', dpi=300, bbox_inches='tight')

plt.show()


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("Data Sales3.csv", delimiter = ";")

# Scatter plot w day against tip
plt.bar(data['Month'], data['Quantity'])

# Adding Title to the plot
plt.title("Bar Chart")

# Setting the X and Y labels
plt.xlabel('Month')
plt.ylabel('Quantity')

# Save the plot as a PNG file
plt.savefig('bar.png', dpi=300, bbox_inches='tight')

plt.show()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("Data Sales3.csv", delimiter = ";")

# Scatter plot w day against tip
plt.hist(data['Month'])


# Adding Title to the plot
plt.title("Histogram")

# Save the plot as a PNG file
plt.savefig('histogram.png', dpi=300, bbox_inches='tight')

plt.show()


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("Data Sales3.csv", delimiter = ";")

# Scatter plot w day against tip
sales = ['Month', 'Quantity']
datasales = [23, 10]

plt.pie(datasales, labels=sales)

plt.title("Sales Data")

# Save the plot as a PNG file
plt.savefig('pie.png', dpi=300, bbox_inches='tight')

plt.show()


# In[ ]:




