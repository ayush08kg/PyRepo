import requests
#api key from https://ipgeolocation.io/ 
api_key="9378ed4e6c4b4387ad8f2ea8f09ceff1"
#file handling
try:
    file = open("pro1.txt","r")
    data = file.read()
# All IPs used inside text file is valid except the last one
    sp = data.split()
    for i in range(0,len(sp)):
        print("IP: ",sp[i])
        ip_addr=sp[i]
        response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_addr}")
        if response.status_code == 200:
            data = response.json()
            print(f"Country: {data.get('country_name')}")
            print(f"Latitudes: {data.get('latitude')}")
            print(f"Longitudes: {data.get('longitude')}")
            print()
        else:
        #Last IP is madeup to run this block
            print(f"Request ERROR: {response.status_code}")

except IOError:
    print("File access problem")
