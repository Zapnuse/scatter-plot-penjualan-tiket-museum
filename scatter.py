import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv('/content/drive/MyDrive/Visdas/data-rekapitulasi-hasil-penjualan-tiket-masuk-museum-di-dki-jakarta-tahun-2010.csv')

# create scatter plot
plt.scatter(df['tahun'], df['nilai_penjualan'], alpha=0.5)
plt.title('Grafik Penjualan')
plt.xlabel('tahun')
plt.ylabel('Jumlah Penjualan')

# show plot
plt.show()
