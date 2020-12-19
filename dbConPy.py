import pymssql
import pandas as pd
import keyring

conn = pymssql.connect(server='ec2-18-233-185-214.compute-1.amazonaws.com', user="vb_xuy", password=keyring.get_password("HawkPWD", "vb_xuy"), database='hawk_rnd')

df = pd.read_sql('SELECT TOP 100 ID, PitchNo, Pitcher, RelSpeed, SpinRate From Trackman', con=conn)

print(df.head(10))