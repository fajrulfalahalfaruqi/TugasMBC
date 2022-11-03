def volume_kubus(p,l,t):
    hasil=(p*l*t)
    return hasil

p=int(input("Masukkan nilai panjang:"))
l=int(input("Masukkan nilai lebar:"))
t=int(input("Masukkan nilai tinggi:"))

print("Volume Kubus", volume_kubus(p,l,t))
