n=input()
hour=6*n/3.14
minut=60*(6*n/3.14-hour)
angle=minut*3.14/30
print round(angle,1)
print hour,minut
