def volume_kubus(p,l,t):
    hasil=(p*l*t)
    return hasil

p=int(input("Masukkan Nilai Panjang:"))
l=int(input("Masukkan Nilai Lebar:"))
t=int(input("Masukkan Nilai Tinggi:"))

print("Volume Kubus", volume_kubus(p,l,t))
