import pandas as pd 
s=pd.Series([10,20,30,40])
print(s) 
manual_indexcing=pd.Series([10,20,30],["hey","haa","hi"])
print(manual_indexcing)
print("\n")
import pandas as pd

# Creating a simple DataFrame
data = {
    "Name": ["Sid", "Ram", "Shyam"],
    "Age": [21, 22, 23],
    "City": ["Pune", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)

print(df)
print("\nShape:", df.shape)