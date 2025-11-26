import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Dette skifter backend til en, der normalt fungerer godt på de fleste systemer
import matplotlib.pyplot as plt
import hsi_mod_til_Soren as hsi


sti = "C:/Dokumenter/Mikro_hsi/Frimaerke/" #Mappen aendres her
navn = "_HSI_hsi25072402"   #Filnavnet aendres her
fl = sti + navn + ".pam"

data, H, B, W = hsi.read_pam_file(fl)
print(data.shape)

billede = hsi.GrayHyperImage(data,1296)
plt.imshow(billede)
plt.show()
