import matplotlib.pyplot as plt
import cv2

img = cv2.imread('Prueba2.jpg', 0) #o 0 transforma a imagem em P&B
cv2.imshow("imagm P&B", img)

#Calcular o gráfico
k = cv.calcHist([img], [0], none, [256], [0,256])

plt.figure()
plt.title("Histograma P&B")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(k)
plt.xlim([0,256])
plt.show()

cv2.waitKey(0) 
