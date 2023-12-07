from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    data = {
        "nodes": {},
        "distance": 0,
        "time": 0,
        "paths": [],
        "url": '',
    }

    carregar_cidades_caminhos()

    if 'origem' in request.args and 'destino' in request.args:
        origem_id = request.args.get('origem', "0")
        destino_id = request.args.get('destino', "0")
        data["distance"], caminho = grafo.dijkstra(int(origem_id), int(destino_id))
        data["nodes"], data["paths"], data["time"] = grafo.carregar_rota(caminho)

        data["url"] = grafo.rota_google(data["nodes"])
    else:
        data["nodes"] = grafo.vertices 
        data["paths"] = grafo.pegar_caminhos()

    return render_template('index.html', nodes=data["nodes"], cities=cities, paths=data["paths"], distancia=data["distance"], tempo=data["time"], url=data["url"])

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

    def remover_vertice(self, vertice_id):
        for chave in self.vertices.items():
            if chave == vertice_id:
                for caminho in self.vertices[vertice_id]["paths"]:
                    if caminho["to"] == vertice_id:
                        self.vertices[vertice_id]["paths"].remove(caminho)


    def adicionar_aresta(self, idOrigem, idDestino, distancia, tempo, arestaId):
        if idOrigem in self.vertices and idDestino in self.vertices:
            self.vertices[idOrigem]["paths"].append({"id": arestaId,"from": idOrigem, "to": idDestino, "distance": distancia, "time": tempo})
            self.vertices[idDestino]["paths"].append({"id": arestaId,"from": idDestino, "to": idOrigem, "distance": distancia, "time": tempo})

    def dijkstra(self, inicio, fim):
        distancia = {v: float('infinity') for v in self.vertices}
        distancia[inicio] = 0
        visitados = set()

        while len(visitados) < len(self.vertices):
            atual = min((v for v in self.vertices if v not in visitados), key=distancia.get)
            visitados.add(atual)

            for vizinho in self.vertices[atual]["paths"]:
                peso = vizinho["distance"]
                proximo_vertice = vizinho["to"]

                if distancia[atual] + peso < distancia[proximo_vertice]:
                    distancia[proximo_vertice] = distancia[atual] + peso

        distancia_total = distancia[fim]
        caminho_minimo = self.reconstruir_caminho(inicio, fim, distancia)
        return distancia_total, caminho_minimo

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
    
    def carregar_rota(self, vertices):
        novos_vertices = {}
        novos_caminhos = []
        tempo_total = 0
        for posicao_vertice in range(len(vertices)):
            id_vertice_atual = vertices[posicao_vertice]
            vertice_atual = {}

            for key, vertice in self.vertices.items():
                if id_vertice_atual == key:
                    vertice_atual = vertice

            if id_vertice_atual != vertices[-1]:
                id_proximo_vertice = vertices[posicao_vertice+1]

                for path in vertice_atual["paths"]:
                    if path["from"] == id_vertice_atual and path["to"] == id_proximo_vertice:
                        vertice_atual["paths"] = [path]
                        novos_caminhos.append(path)
                        tempo_total = tempo_total + path["time"]
                        break
            else:
                vertice_atual["paths"] = []
            novos_vertices[id_vertice_atual] = vertice_atual

        return novos_vertices, novos_caminhos, tempo_total
    
    def pegar_caminhos(self):
        caminhos = []
        for chave, vertice in self.vertices.items():

            for caminho in vertice["paths"]:
                ja_tem = False
                ids_vertices = [caminho["from"], caminho["to"]]

                for cam in caminhos:
                    if cam["from"] in ids_vertices and cam["to"] in ids_vertices:
                        ja_tem = True

                if not ja_tem:
                    caminhos.append(caminho)

        return caminhos
    
    def rota_google(self, vertices):
        url = 'https://www.google.com.br/maps/dir/'
        for chave, vertice in vertices.items():
            url += f"{vertice["geolocation"]["lat"],vertice["geolocation"]["lon"]}/"
        return url
                
cities = [
    {
        "id": 1,
        "name":"Gama",  
        "coordinates": {            
            'x':611,
            'y':725
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
            'x':591,
            'y':417
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
            'x':291,
            'y':80
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
            'x':722,
            'y':274
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
            'x':653,
            'y':333
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
            'x':858,
            'y':310
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
            'x':664,
            'y':431
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
            'x':492,
            'y':378
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
            'x':763,
            'y':422
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
            'x':535,
            'y':502
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
            'x':146,
            'y':242
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
            'x':1120,
            'y':508
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
            'x':587,
            'y':587
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
            'x':932,
            'y':382
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
            'x':977,
            'y':259
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
        "time": 10, 
        "distance": 10,
    },
    {
        "id": "b",
        "from": 13, 
        "to": 10, 
        "time": 12, 
        "distance": 8,
    },
     {
        "id": "c",
        "from": 10, 
        "to": 8, 
        "time": 14, 
        "distance": 9,
    },
     {
        "id": "d",
        "from": 10, 
        "to": 2, 
        "time": 13, 
        "distance": 9,
    },
     {
        "id": "e",
        "from": 8, 
        "to": 2, 
        "time": 12, 
        "distance": 8,
    },
     {
        "id": "f",
        "from": 8, 
        "to": 11, 
        "time":26, 
        "distance": 26,
    },
     {
        "id": "g",
        "from": 8, 
        "to": 3, 
        "time":30, 
        "distance": 25,
    },
     {
        "id": "h",
        "from": 11, 
        "to": 3, 
        "time":23, 
        "distance": 11,
    },
     {
        "id": "i",
        "from":2, 
        "to": 5, 
        "time":11, 
        "distance": 7,
    },
     {
        "id": "j",
        "from": 2, 
        "to": 7, 
        "time": 8, 
        "distance": 4,
    },
     {
        "id": "k",
        "from": 5, 
        "to": 4, 
        "time": 14, 
        "distance": 8,
    },
     {
        "id": "l",
        "from": 7, 
        "to": 9, 
        "time": 12, 
        "distance": 8,
    },
     {
        "id": "m",
        "from": 4, 
        "to": 9, 
        "time": 10, 
        "distance": 6,
    },
     {
        "id": "n",
        "from": 9, 
        "to": 6, 
        "time": 12, 
        "distance": 8,
    },
     {
        "id": "o",
        "from": 6, 
        "to": 15, 
        "time": 17, 
        "distance": 12,
    },
     {
        "id": "p",
        "from": 6, 
        "to": 14, 
        "time": 13, 
        "distance": 7,
    },
     {
        "id": "q",
        "from": 14, 
        "to": 15, 
        "time": 12, 
        "distance": 8,
    },
     {
        "id": "r",
        "from": 14, 
        "to": 12, 
        "time": 19, 
        "distance": 17,
    },
]


grafo = Grafo()

def carregar_cidades_caminhos():
    grafo.vertices = {}

    for city in cities:
        grafo.adicionar_vertice(city)

    for path in paths:
        grafo.adicionar_aresta(path["from"],path["to"],path["distance"],path["time"],path["id"])

if __name__ == '__main__':
    app.run(debug=True)

