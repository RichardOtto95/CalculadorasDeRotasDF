from flask import Flask, render_template, redirect, request, url_for
import heapq

app = Flask(__name__)


@app.route('/')
def index():
    dijkstra = {
        "path": [],
        "distance":0
    }

    if 'origem' in request.args and 'destino' in request.args:
        origem_id = request.args.get('origem', "0")
        destino_id = request.args.get('destino', "0")
        dijkstra = grafo.dijkstra(int(origem_id), int(destino_id))

    return render_template('index.html', nodes=grafo.vertices, cities=cities, paths=paths, rotas=dijkstra["path"], distancia=dijkstra["distance"])

@app.route('/rota')
def rota():
    origem_id = request.args.get('origem', '0')
    destino_id = request.args.get('destino', '0')
    return redirect(url_for('index', origem=origem_id, destino=destino_id))

class Grafo:
    def __init__(self):
        self.vertices = {}
        
    def adicionar_vertice(self, vertice):
        if vertice["id"] not in self.vertices:
            self.vertices[vertice["id"]] = vertice

    def adicionar_aresta(self, idOrigem, idDestino, distancia, tempo, arestaId):
        if idOrigem in self.vertices and idDestino in self.vertices:
            self.vertices[idOrigem]["paths"].append({"id": arestaId,"from": idOrigem, "to": idDestino, "distance": distancia, "time": tempo})
            self.vertices[idDestino]["paths"].append({"id": arestaId,"from": idDestino, "to": idOrigem, "distance": distancia, "time": tempo})

    def dijkstra(self, inicio, fim):
        distancia = {v: float('infinity') for v in self.vertices}
        distancia[inicio] = 0
        visitados = set()

        while len(visitados) < len(self.vertices):
            atual = min((v for v in self.vertices if v not in visitados), key=lambda v: distancia[v])
            visitados.add(atual)

            for vizinho in self.vertices[atual]["paths"]:
                peso = vizinho["distance"]
                proximo_vertice = vizinho["to"]

                if distancia[atual] + peso < distancia[proximo_vertice]:
                    distancia[proximo_vertice] = distancia[atual] + peso

        distancia_total = distancia[fim]
        caminho_minimo = self.reconstruir_caminho(inicio, fim, distancia)
        return {"distance": distancia_total,"path": caminho_minimo}

    def reconstruir_caminho(self, inicio, fim, distancia):
        caminho_minimo = []
        atual = fim
        while atual is not None:
            caminho_minimo.insert(0, atual)
            vizinhos = [v for v in self.vertices[atual]["paths"] if distancia[v["to"]] == distancia[atual] - v["distance"]]
            if vizinhos:
                atual = vizinhos[0]["to"]
            else:
                atual = None
        return caminho_minimo

cities = [
    {
        "id": 1,
        "name":"Gama",  
        "coordinates": {            
            'x':442,
            'y':613
        },
        "geolocation": {
            "lat":-15.959459,
            "lon":-48.044531,
        },
        "paths": []
    },
    {
        "id": 2,
        "name":"Taguatinga",  
        "coordinates": {
            'x':406,
            'y':454
        },
        "geolocation": {
            "lat":-15.833188,
            "lon":-48.056530,
        },
        "paths": []
    },
    {
        "id": 3,
        "name":"Brazlândia",  
        "coordinates": {
            'x':266,
            'y':285
        },
        "geolocation": {
            "lat":-15.680762,
            "lon":-48.203499,
        },
        "paths": []
    },
    {
        "id": 4,
        "name":"Estrutural",  
        "coordinates": {
            'x':493,
            'y':391
        },
        "geolocation": {
            "lat":-15.781653,
            "lon":-47.997471,
        },
        "paths": []
    },
    {
        "id": 5,
        "name":"Vicente_pires",  
        "coordinates": {
            'x':446,
            'y':429
        },
        "geolocation": {
            "lat":-15.808725,
            "lon":-48.032145,
        },
        "paths": []
    },
    {
        "id": 6,
        "name":"Cruzeiro",  
        "coordinates": {
            'x':572,
            'y':419
        },
        "geolocation": {
            "lat":-15.793829,
            "lon":-47.937544,
        },
        "paths": []
    },
    {
        "id": 7,
        "name":"Águas_Claras",  
        "coordinates": {
            'x':457,
            'y':469
        },
        "geolocation": {
            "lat":-15.840042,
            "lon":-48.028344,
        },
        "paths": []
    },    
    {
        "id":8,
        "name":"Ceilândia",  
        "coordinates": {
            'x':306,
            'y':446
        },
        "geolocation": {
            "lat":-15.819392,
            "lon":-48.108464,
        },
        "paths": []
    },
    {
        "id": 9,
        "name":"Guará",  
        "coordinates": {
            'x':516,
            'y':476
        },
        "geolocation": {
            "lat":-15.815048,
            "lon":-47.986385,
        },
        "paths": []
    },
    {
        "id": 10,
        "name":"Samambaia",  
        "coordinates": {
            'x':351,
            'y':537
        },
        "geolocation": {
            "lat":-15.873742,
            "lon":-48.085019,
        },
        "paths": []
    },
    {
        "id": 11,
        "name":"Águas_lindas",  
        "coordinates": {
            'x':142,
            'y':375
        },
        "geolocation": {
            "lat":-15.735889,
            "lon":-48.274264,
        },
        "paths": []
    },
    {
        "id": 12,
        "name":"São_Sebastião",  
        "coordinates": {
            'x':703,
            'y':524
        },
        "geolocation": {
            "lat":-15.885826,
            "lon":-47.821175,
        },
        "paths": []
    },
    {
        "id": 13,
        "name":"Recanto_das_Emas",  
        "coordinates": {
            'x':377,
            'y':566
        },
        "geolocation": {
            "lat":-15.901852,
            "lon":-48.061782,
        },
        "paths": []
    },
    {
        "id": 14,
        "name":" Asa_sul",  
        "coordinates": {
            'x':599,
            'y':459
        },
        "geolocation": {
            "lat":-15.812628,
            "lon":-47.896467,
        },
        "paths": []
    },
    {
        "id": 15,
        "name":" Asa_norte",  
        "coordinates": {
            'x':623,
            'y':384
        },
        "geolocation": {
            "lat":-15.764431,
            "lon":-47.870308,
        },
        "paths": []
    },
]


paths = [
    {
        "id": "a",
        "from": 1, 
        "to": 13, 
        "distance": 10, 
        "time": 10
    },
    {
        "id": "b",
        "from": 13, 
        "to": 10, 
        "distance": 12, 
        "time": 8.6
    },
     {
        "id": "c",
        "from": 10, 
        "to": 8, 
        "distance": 14, 
        "time": 9.4
    },
     {
        "id": "d",
        "from": 10, 
        "to": 2, 
        "distance": 13, 
        "time": 9.4
    },
     {
        "id": "e",
        "from": 8, 
        "to": 2, 
        "distance": 12, 
        "time": 8.2
    },
     {
        "id": "f",
        "from": 8, 
        "to": 11, 
        "distance":26, 
        "time": 26.4
    },
     {
        "id": "g",
        "from": 8, 
        "to": 3, 
        "distance":30, 
        "time": 25.8
    },
     {
        "id": "h",
        "from": 11, 
        "to": 3, 
        "distance":23, 
        "time": 11.8
    },
     {
        "id": "i",
        "from":2, 
        "to": 5, 
        "distance":11, 
        "time": 7.8
    },
     {
        "id": "j",
        "from": 2, 
        "to": 7, 
        "distance": 8, 
        "time": 4.3
    },
     {
        "id": "k",
        "from": 5, 
        "to": 4, 
        "distance": 14, 
        "time": 8.4
    },
     {
        "id": "l",
        "from": 7, 
        "to": 9, 
        "distance": 12, 
        "time": 8.6
    },
     {
        "id": "m",
        "from": 4, 
        "to": 9, 
        "distance": 10, 
        "time": 6.1
    },
     {
        "id": "n",
        "from": 9, 
        "to": 6, 
        "distance": 12, 
        "time": 8.5
    },
     {
        "id": "o",
        "from": 6, 
        "to": 15, 
        "distance": 17, 
        "time": 12.4
    },
     {
        "id": "p",
        "from": 6, 
        "to": 14, 
        "distance": 13, 
        "time": 7.9
    },
     {
        "id": "q",
        "from": 14, 
        "to": 15, 
        "distance": 12, 
        "time": 8.5
    },
     {
        "id": "r",
        "from": 14, 
        "to": 12, 
        "distance": 19, 
        "time": 17.1
    },
]

grafo = Grafo()

for city in cities:
    grafo.adicionar_vertice(city)

for path in paths:
    grafo.adicionar_aresta(path["from"],path["to"],path["distance"],path["time"],path["id"])

if __name__ == '__main__':
    app.run(debug=True)
