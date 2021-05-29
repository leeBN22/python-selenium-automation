'''
h = 0
m = 1
s = 1

result = 61000
'''

def time(s,m,h):
    ms_h =0
    ms_m =0
    ms_s =0
    if (h <= 23 and h >=0):
        s_h = h * 3600
        ms_h = s_h * 1000
    if (m <= 59 and m >= 0):
        s_m = m * 60
        ms_m= s_m * 1000
    if (s <= 59 and s >= 0):
        ms_s = s * 1000
    else:
        print("Enter the correct values for Hour, Minute, Second")
        return
    result = ms_h + ms_m + ms_s
    return result

h = int(input('Please enter Hour between 0 and 23 (both inclusive): '))
m = int(input('Please enter Minute between 0 and 59 (both inclusive): '))
s = int(input('Please enter Second between 0 and 59 (both inclusive): '))
print("Time in Milliseconds: " + str(time(s,m,h)) + " ms")