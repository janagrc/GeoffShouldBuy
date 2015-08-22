import numpy as np

origin = ['Danish','Swedish','German','Swiss','American','Brazilian']

appearance = ['matte', 'stainless', 'weathered', 'hand-crafted']

material = ['wood', 'steel', 'composite', 'paper']

product = ['alcohol', 'furniture', 'computers', 'shoes', 'wallets']

print('Geoff should buy ' + origin[np.random.randint(len(origin))] + ' ' + appearance[np.random.randint(len(appearance))] + ' ' + material[np.random.randint(len(material))] + ' ' + product[np.random.randint(len(product))])
