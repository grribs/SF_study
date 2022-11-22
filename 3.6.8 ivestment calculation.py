i = 1000
n = 3000
st = 0.08
yr = 0
while i < n:
    st = i * 0.08
    i += st
    yr += 1
    print(round(i, 2))
print(yr)


