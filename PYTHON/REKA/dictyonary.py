def aa():
    print"Dictionary"


no_telpon={"nama" : ["Jane Doe", "Jhon Smith", "Bob Stone"],"Telephone Number" : ["+27 555 5367", "+27 555 6254", "+27 555 5689"]}
no_telpon["Telephone Number"][0] = "+27 555 1024"
print(no_telpon)
no_telpon.update({ "nama": ["Jane Doe", "Jhon Smith", "Bob Stone", "Anna Cooper"], "Telephone Number": ["+27 555 1024", "+27 555 6254", "+27 555 5689", "+27 555 3237"]})
print(no_telpon)
print(no_telpon["Telephone Number"][2])
print(no_telpon.keys())
print(no_telpon.values())
