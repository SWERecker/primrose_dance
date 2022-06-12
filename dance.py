import os
import random
import json
import sys
use_bp = 0
# if len(sys.argv) > 1:
#     use_bp = int(sys.argv[1])
dances = []


def load_dance():
    with open('dance.csv', 'r', encoding='utf-8') as dance:
        dance_data = dance.readlines()
    for l in dance_data:
        data = l.replace('%', '').strip().split(',')
        dances.append({
            "name": data[0],
            "0": data[1],
            "1": data[2],
            "2": data[3],
            "3": data[4],
        })
    random.shuffle(dances)

def dance(bp=0):
    result = []
    while not len(result) > bp:
        d = random.choice(dances)
        x = random.random() * 100
        if x < float(d[str(bp)]):
            result.append(d['name'])
    return result


if __name__ == '__main__':
    load_dance()
    #    res = {}
    #    for i in range(10000):
    #        a = dance(3)
    #        if a in res:
    #            res[a] += 1
    #        else:
    #            res[a] = 1
    # print(json.dumps(res, indent=4, ensure_ascii=False))
    last_bp = 0
    while True:
        try:
            use_bp = int(input(f'请输入使用的BP[{last_bp}]:'))
        except KeyboardInterrupt:
            sys.exit()
        except:
            use_bp = last_bp
        if use_bp in [0, 1, 2, 3]:
            dance_result = dance(use_bp)
            for r in dance_result:
                print(r)
            print('=' * 50)
            last_bp = use_bp
        else:
            print('请输入0/1/2/3')
