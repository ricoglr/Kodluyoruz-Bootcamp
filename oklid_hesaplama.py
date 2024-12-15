import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Noktaların listesi
points = [(1, 2), (4, 6), (5, 1), (7, 7), (2, 3)]

# Mesafeleri hesaplayıp saklamak için bir liste
distances = []

# Tüm nokta çiftleri arasındaki mesafeyi hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı noktayı tekrar hesaplamamak için j=i+1'den başlıyoruz
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bul
min_distance = min(distances)

# Sonucu yazdır
print(f"Tüm noktalar arasındaki minimum Öklid mesafesi: {min_distance:.2f}")
