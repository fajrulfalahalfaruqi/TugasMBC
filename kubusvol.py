def volume_kubus(p,l,t):
    hasil=(p*l*t)
    return hasil

p=int(input("masukkan nilai panjang:"))
l=int(input("masukkan nilai lebar:"))
t=int(input("masukkan nilai tinggi:"))

print("Volume Kubus", volume_kubus(p,l,t))
