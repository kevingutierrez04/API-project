heroes = {
  'Moira' : 'support',
  'Sombra' : 'dps',
  'Zarya' : 'tank'
}

print('With the keys method:')
for key in heroes.keys():
  print(f'\t{key} -> {type(key)}')

print('\nWithout the keys method:')
for key in heroes:
  print(f'\t{key} -> {type(key)}')