from re import findall

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

with open('medias.txt', 'w') as f:
    f.write('-- Media de idades --\n')
    f.write(f'Global: { round(sum(idadesFlat) / len(idadesFlat)) }\n')
    f.write(f'Mulheres: { round(sum(idades[0]) / len(idades[0])) }\n')
    f.write(f'Homens: { round(sum(idades[1]) / len(idades[1])) }\n')

    f.write('\n')

    f.write('-- Media de pesos --\n')
    f.write(f'Global: { round(sum(pesosFlat) / len(pesosFlat))}\n')
    f.write(f'Mulheres: { round(sum(pesos[0]) / len(pesos[0])) }\n')
    f.write(f'Homens: { round(sum(pesos[1]) / len(pesos[1])) }\n')