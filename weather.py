import urllib2
import json

key = urllib2.urlopen('YOUR-API-KEY-AND-LOCATION-OF-CHOICE') #grabbing the weather via api call

json_string = key.read()
parsed_json = json.loads(json_string)

location = parsed_json['location']['city'] #picking out our location/city
temp_c = parsed_json['current_observation']['temp_c'] #Current Temp
condition = parsed_json['current_observation']['weather']#Current Weather

print "Current conditions in %s:" % location #print out the data
print " %dC and %s" % (temp_c, condition)
key.close()
