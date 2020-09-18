from search.models import Maps

cities_dict = {
 'Aguas Mornas': {'lat': -27.743632, 'lng': -48.9202828},
 'Alfredo Wagner': {'lat': -27.6959489, 'lng': -49.33206939999999},
 'Angelina': {'lat': -27.5733359, 'lng': -48.9843789},
 'Anitapolis': {'lat': -27.9071185, 'lng': -49.128297},
 'Antonio Carlos': {'lat': -27.5179042, 'lng': -48.7684179},
 'Ararangua': {'lat': -28.9361187, 'lng': -49.4923013},
 'Armazem': {'lat': -28.2630149, 'lng': -49.0198837},
 'Balneario Arroio Do Silva': {'lat': -28.9811481, 'lng': -49.4241809},
 'Balneario Gaivota': {'lat': -29.1546867, 'lng': -49.5809106},
 'Biguacu': {'lat': -27.4955748, 'lng': -48.65536849999999},
 'Braco Do Norte': {'lat': -28.2793737, 'lng': -49.1575402},
 'Canelinha': {'lat': -27.2618213, 'lng': -48.7653683},
 'Capivari De Baixo': {'lat': -28.4605555, 'lng': -48.9505159},
 'Cocal Do Sul': {'lat': -28.5994838, 'lng': -49.3238948},
 'Criciuma': {'lat': -28.6727702, 'lng': -49.3733771},
 'Ermo': {'lat': -28.984951, 'lng': -49.6423481},
 'Florianopolis': {'lat': -27.5986393, 'lng': -48.5187229},
 'Forquilhinha': {'lat': -28.7477963, 'lng': -49.4745059},
 'Garopaba': {'lat': -28.0272534, 'lng': -48.6189508},
 'Governador Celso Ramos': {'lat': -27.3159368, 'lng': -48.5571297},
 'Grão Para': {'lat': -28.1856432, 'lng': -49.216393},
 'Gravatal': {'lat': -28.3228006, 'lng': -49.0669423},
 'Icara': {'lat': -28.7137096, 'lng': -49.3091437},
 'Imarui': {'lat': -28.3437512, 'lng': -48.8164937},
 'Imbituba': {'lat': -28.227627, 'lng': -48.6691286},
 'Jacinto Machado': {'lat': -29.0003303, 'lng': -49.76115799999999},
 'Jaguaruna': {'lat': -28.6188549, 'lng': -49.0250549},
 'Laguna': {'lat': -28.4876062, 'lng': -48.8397403},
 'Lauro Muller': {'lat': -28.3919058, 'lng': -49.3960964},
 'Leoberto Leal': {'lat': -27.5048201, 'lng': -49.2883819},
 'Major Gercino': {'lat': -27.4398664, 'lng': -49.1019233},
 'Maracaja': {'lat': -28.8475807, 'lng': -49.45456069999999},
 'Meleiro': {'lat': -28.8564935, 'lng': -49.5891233},
 'Morro Da Fumaca': {'lat': -28.6540002, 'lng': -49.2120154},
 'Morro Grande': {'lat': -28.8010724, 'lng': -49.7218557},
 'Nova Trento': {'lat': -27.3069805, 'lng': -49.0009403},
 'Nova Veneza': {'lat': -28.6370917, 'lng': -49.5010759},
 'Orleans': {'lat': -28.3586648, 'lng': -49.288187},
 'Palhoca': {'lat': -27.646431, 'lng': -48.67191680000001},
 'Passo De Torres': {'lat': -29.3207869, 'lng': -49.7239294},
 'Paulo Lopes': {'lat': -27.9604166, 'lng': -48.6789114},
 'Pedras Grandes': {'lat': -28.4343651, 'lng': -49.1953975},
 'Praia Grande': {'lat': -29.1951531, 'lng': -49.9475655},
 'Rancho Queimado': {'lat': -27.6735003, 'lng': -49.0124253},
 'Rio Fortuna': {'lat': -28.1340254, 'lng': -49.10375190000001},
 'Sangão': {'lat': -28.6381455, 'lng': -49.1257517},
 'Santa Rosa De Lima': {'lat': -28.0122447, 'lng': -49.1828385},
 'Santa Rosa Do Sul': {'lat': -29.1382661, 'lng': -49.7151971},
 'Santo Amaro Da Imperatriz': {'lat': -27.6856839, 'lng': -48.7817857},
 'São Bonifacio': {'lat': -27.9001105, 'lng': -48.9301287},
 'São João Batista': {'lat': -27.2758367, 'lng': -48.850354},
 'São João Do Sul': {'lat': -29.2243477, 'lng': -49.8101067},
 'São Jose': {'lat': -27.6140791, 'lng': -48.6370861},
 'São Ludgero': {'lat': -28.3274045, 'lng': -49.1789665},
 'São Martinho': {'lat': -28.109123, 'lng': -49.0211225},
 'São Pedro De Alcantara': {'lat': -27.5852252, 'lng': -48.8296806},
 'Sideropolis': {'lat': -28.5960038, 'lng': -49.4319132},
 'Sombrio': {'lat': -29.0978736, 'lng': -49.6401083},
 'Tijucas': {'lat': -27.240063, 'lng': -48.63361829999999},
 'Timbe Do Sul': {'lat': -28.829251, 'lng': -49.8425427},
 'Treviso': {'lat': -28.5141107, 'lng': -49.4572672},
 'Treze De Maio': {'lat': -28.5597196, 'lng': -49.1499529},
 'Tubarão': {'lat': -28.4818875, 'lng': -49.0058727},
 'Turvo': {'lat': -28.9278045, 'lng': -49.68203459999999},
 'Urussanga': {'lat': -28.525676, 'lng': -49.3215835}
}

search_words = [
]


f = open('key.txt', mode='r')
key = f.read()
f.close()

maps = Maps(key)

maps.read_places_from_csv('places.csv')

for word in search_words:
    for city in cities_dict.values():
        maps.find_places(text=word, location=f"{city['lat']},{city['lng']}")

maps.more_information_places()

maps.save_to_csv('places.csv')