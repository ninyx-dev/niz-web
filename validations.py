'''
Created on 2011. 9. 25.

@author: ninyx
'''
from django.core.exceptions import ValidationError

def validate_gps(value):
    gps_points = value.split(";");
    
    for gps  in gps_points:
        if len(gps.split(",")) != 2:
            raise ValidationError(u'%s %d is not gps point' %( gps, len(gps.split(","))))
    
