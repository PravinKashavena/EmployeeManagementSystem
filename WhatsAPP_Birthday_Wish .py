import pywhatkit as kit
import pandas as pd
from datetime import datetime

# Read the CSV file containing the birthday data
data = pd.read_csv("PG_dbda.csv")

# Get today's date
today = datetime.now().strftime("%d-%m")

l=[]
for x in data['DOB']:
    l.append(x[0:5])

for x in data['DOB']:
    if x[0:5]==today:
        print(data[data['DOB'] == x])
        j=(data[data['DOB'] == x])
        break
for l,k in j.iterrows():
    print(l,k)

# Iterate over birthdays today and send wishes
for index, row in j.iterrows():
     Name = row["Name"]
     whatsapp = str(row["WhatsApp"])  # Correct column name
     message = f"On your special day, I wish you all the happiness life has to offer. Have a fantastic birthday, {Name}! 🎉🎂🥳"

     try:
         kit.sendwhatmsg(f"+{whatsapp}", message, datetime.now( ).hour,datetime.now( ).minute+2)  # Send message at the beginning of the next minute
         print(f"Birthday wishes sent to {Name}")
     except Exception as e:
         print(f"Error sending birthday wishes to {Name}: {e}")
