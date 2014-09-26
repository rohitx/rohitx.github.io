---
layout: post
title: Creating DataFrames in Pandas
---
It is fairly easy to create a DataFrame in Pandas. To create a DataFrame in Pandas, we need to do the following: 

1. Create a list of column headers
2. Create an index associated to the number of rows 
3. Define the dataframe with its parameters

Suppose the dataframe has 100 lines, we would do the following: 

~~~python
import pandas as pd
user_columns = ["name1", "name2", "name3"]
index_user = [i for i in range(1,101)]
df_new = pd.DataFrame(index=index_user, columns=user_columns)
~~~

Now suppose we had another dataframe (i.e. df_old) and we wanted to populate our new dataframe with some of the columns from the old dataframe. Here's how to do that: 

~~~python
df_new["name1"] = df_old["restaurant_names"].values
df_new["name2"] = df_old["Address"].values
~~~

Of course this will work provided the number of rows in each of the dataframes match. 

There we have it. We've created a new dataframe and populated it with values. 

