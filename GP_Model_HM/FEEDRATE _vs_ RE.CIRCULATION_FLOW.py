# For Summer Season

def summer_re_circulation_flow(feedrate):
    if(feedrate>=26 or feedrate<36 ):
       return 3*feedrate +212
    if(feedrate>=36 or feedrate<43 ):
        val= (10*feedrate)
        return val-40

print(summer_re_circulation_flow(26))
print(summer_re_circulation_flow(36))
print(summer_re_circulation_flow(40))
print(summer_re_circulation_flow(42))