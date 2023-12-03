from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nodes = []
    
    for city in cities:
        nodes.append({'id': city['id'],'label': city['name'],'x': (city['coordinates']['x'] ),'y': (city['coordinates']['y'] ),})        

    # print(nodes)
    return render_template('index.html', nodes = nodes, cities = cities)

cities = [
    {
        "id": 1,
        "name":"Gama",  
        "coordinates": {
            # 'x':30,
            # 'y':30
            'x':442,
            'y':613
        },
        "geolocation": {
            "lat":-15.959459,
            "lon":-48.044531,
        }
    },
    {
        "id": 2,
        "name":"Taguatinga",  
        "coordinates": {
            'x':418,
            'y':470
            # 'x':418,
            # 'y':328
        },
        "geolocation": {
            "lat":-15.833188,
            "lon":-48.056530,
        }
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
        }
    },
    # {
    #     "id": 4,
    #     "name":"Estrutural",  
    #     "coordinates": {
    #         'x':0,
    #         'y':0
    #     },
    #     "geolocation": {
    #         "lat":-15.781653,
    #         "lon":-47.997471,
    #     }
    # },
    # {
    #     "id": 5,
    #     "name":"Vicente_pires",  
    #     "coordinates": {
    #         'x':0,
    #         'y':0
    #     },
    #     "geolocation": {
    #         "lat":-15.808725,
    #         "lon":-48.032145,
    #     }
    # },
    # {
    #     "id": 6,
    #     "name":"Cruzeiro",  
    #     "coordinates": {
    #         'x':0,
    #         'y':0
    #     },
    #     "geolocation": {
    #         "lat":-15.793829,
    #         "lon":-47.937544,
    #     }
    # },
    # {
    #     "id": 7,
    #     "name":"Águas_Claras",  
    #     "coordinates": {
    #         'x':0,
    #         'y':0
    #     },
    #     "geolocation": {
    #         "lat":-15.840042,
    #         "lon":-48.028344,
    #     },
    # },    
    # {
    #     "id":8,
    #     "name":"Ceilândia",  
    #     "coordinates": {
    #         'x':0,
    #         'y':0
    #     },
    #     "geolocation": {
    #         "lat":-15.819392,
    #         "lon":-48.108464,
    #     }
    # },
    # {
    #     "id": 9,
    #     "name":"Guará",  
    #     "coordinates": {
    #         'x':0,
    #         'y':0
    #     },
    #     "geolocation": {
    #         "lat":-15.815048,
    #         "lon":-47.986385,
    #     }
    # },
    # {
    #     "id": 10,
    #     "name":"Samambaia",  
    #     "coordinates": {
    #         'x':0,
    #         'y':0
    #     },
    #     "geolocation": {
    #         "lat":-15.873742,
    #         "lon":-48.085019,
    #     }
    # },
    # {
    #     "id": 11,
    #     "name":"Águas_lindas",  
    #     "coordinates": {
    #         'x':0,
    #         'y':0
    #     },
    #     "geolocation": {
    #         "lat":-15.735889,
    #         "lon":-48.274264,
    #     }
    # },
    # {
    #     "id": 12,
    #     "name":"São_Sebastião",  
    #     "coordinates": {
    #         'x':0,
    #         'y':0
    #     },
    #     "geolocation": {
    #         "lat":-15.885826,
    #         "lon":-47.821175,
    #     }
    # },
    # {
    #     "id": 13,
    #     "name":"Recanto_das_Emas",  
    #     "coordinates": {
    #         'x':0,
    #         'y':0
    #     },
    #     "geolocation": {
    #         "lat":-15.901852,
    #         "lon":-48.061782,
    #     }
    # },
    # {
    #     "id": 14,
    #     "name":" Asa_sul",  
    #     "coordinates": {
    #         'x':0,
    #         'y':0
    #     },
    #     "geolocation": {
    #         "lat":-15.812628,
    #         "lon":-47.896467,
    #     }
    # },
    # {
    #     "id": 15,
    #     "name":" Asa_norte",  
    #     "coordinates": {
    #         'x':0,
    #         'y':0
    #     },
    #     "geolocation": {
    #         "lat":-15.764431,
    #         "lon":-47.870308,
    #     }
    # },
]

if __name__ == '__main__':
    app.run(debug=True)
