import json
import config

img_path = f'img/match/{config.id}/game{str(config.game)}/'
round = json.load(open(f'{img_path}/round1.json'))['end']
print(round)