from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans

#Razonamiento Deductivo
def es_equilatero(a, b, c):
    if a == b and b == c:
        return True
    else:
        return False

#Razonamiento Inductivo
def raz_inductivo():
    numeros = [2, 4, 6, 8, 10]
    media = sum(numeros) / len(numeros)
    print(f"La media de la lista es: {media}")

#Aprendizaje Supervisado
def ap_supervizado():
    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Precisión del modelo: {accuracy}")

#Aprendizaje No Supervisado
def ap_nosuper():
    X = [[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]]

    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    print(centroids)
    print(labels)

op=input("Que tipo de razonamiento o aprendizaje deseas intentar:\n1.-Razonamiento Deductivo\n2.-Razonamiento Inductivo\n3.-Aprendizaje Supervisado\n4.-prendizaje No Supervisado\n ")
if op == '1':
    lado1 = 5
    lado2 = 5
    lado3 = 5

    if es_equilatero(lado1, lado2, lado3):
        print("Es un triángulo equilátero")
    else:
        print("No es un triángulo equilátero")
elif op == '2':
    raz_inductivo()
elif op == '3':
    ap_supervizado()
elif op == '4':
    ap_nosuper()
else:
    print("No existe esa opcion :)")

    

