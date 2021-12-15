from re import findall
import pickle

dados = {
    'Mulheres': {
        'idades': [],
        'pesos': []
    },
    'Homens': {
        'idades': [],
        'pesos': []
    }
}
k = 'Mulheres'

with open('info.txt') as f:
    linhas = f.readlines()

    for linha in linhas:
        matches = findall(r'(\w+)=(\d{1,3}),(\d{1,3})', linha)

        if not len(matches):
            if 'Mulheres' in linha:
                k = 'Mulheres'
            elif 'Homens' in linha:
                k = 'Homens'
        else:
            dados[k]['idades'].append( int(matches[0][1]) )
            dados[k]['pesos'].append( int(matches[0][2]) )

valsKey = lambda key: map(lambda d: d[key], dados.values())
flatten = lambda lst: [item for sublist in lst for item in sublist]

idades = list(valsKey('idades'))
pesos = list(valsKey('pesos'))

idadesFlat = flatten(idades)
pesosFlat = flatten(pesos)

tuploIdades = ('idades', sum(idadesFlat) / len(idadesFlat), sum(idades[0]) / len(idades[0]), sum(idades[1]) / len(idades[1]))
tuploPesos = ('pesos', sum(pesosFlat) / len(pesosFlat), sum(pesos[0]) / len(pesos[0]), sum(pesos[1]) / len(pesos[1]))
with open('medias.bin', 'wb') as f:
    pickle.dump(tuploIdades, f)
    pickle.dump(tuploPesos, f)

# with open('medias.bin', 'rb') as f:
#     idades = pickle.load(f)
#     pesos = pickle.load(f)
#     print(idades, pesos)