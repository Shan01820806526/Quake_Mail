import pandas as pd
import time as tm
import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    """Email alert function from your example"""
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "chowdhuryshantunu51@gmail.com"
    msg['from'] = user
    password = "pjgl czjx zsbr vhzw"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Fixed typo: was startls()
    server.login(user, password)  # Fixed typo: was logln()
    server.send_message(msg)
    server.quit()
    
if __name__=='__main__':
    email_alert("BE ALERT","EARTHQUAKE HAPPENING","anindya.baidya2016@gmail.com")


def earthquake_monitor():
    """Your earthquake monitoring function"""
    while True:
        try:
            df = pd.read_csv('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv')
            reqDF = df[['latitude', 'longitude', 'mag']]
            
            # Bangladesh coordinates (adjust as needed)
            target_lat = 23.8103
            target_lon = 90.4125
            margin = 2.0
            
            lat_filter = (reqDF['latitude'].between(target_lat - margin, target_lat + margin))
            lon_filter = (reqDF['longitude'].between(target_lon - margin, target_lon + margin))
            mag_filter = (reqDF['mag'] > 4)
            
            filtered = df[lat_filter & lon_filter & mag_filter]
            
            if not filtered.empty:
                for _, quake in filtered.iterrows():
                    body = (f"Earthquake Detected!\n\n"
                           f"Magnitude: {quake['mag']}\n"
                           f"Location: Latitude {quake['latitude']}, Longitude {quake['longitude']}\n")
                    email_alert("🚨 Earthquake Alert!", body, "u1801106@student.cvet.ac.bd")
                tm.sleep(60)
            else:
                print(f"No earthquakes detected. Last checked: {tm.ctime()}")
                tm.sleep(300)
                
        except Exception as e:
            print(f"Error occurred: {e}")
            tm.sleep(60)


      
      
      
      
      
      
      
      
      
      