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

print('-- Media de idades --')
print(f'Global: { round(sum(idadesFlat) / len(idadesFlat)) }')
print(f'Mulheres: { round(sum(idades[0]) / len(idades[0])) }')
print(f'Homens: { round(sum(idades[1]) / len(idades[1])) }')

print()

print('-- Media de pesos --')
print(f'Global: { round(sum(pesosFlat) / len(pesosFlat))}')
print(f'Mulheres: { round(sum(pesos[0]) / len(pesos[0])) }')
print(f'Homens: { round(sum(pesos[1]) / len(pesos[1])) }')