import random
import matplotlib.pyplot as plt
import math
import numpy as np

random_list = ['random', 'uniform', 'triangular', 'betabariate', 'expovariate', 'gammavariate', 'gauss', 'lognormvariate', 'normalvariate', 'vonmisesvariate', 'paretovariate', 'weibullvariate']

#random_list = ['lognormvariate']


def generate_random_number(f):
    """ランダム値を1000個生成
        各関数のパラメータは適当に決め打ち。
    """
    if f == 'random':
        return [random.random() for n in range(1000)]
    elif f == 'uniform':
        return [random.uniform(10, 20) for n in range(1000)]
    elif f == 'triangular':
        return [random.triangular(0, 1) for n in range(1000)]
    elif f == 'betabariate':
        return [random.betavariate(4, 7) for n in range(1000)]
    elif f == 'expovariate':
        return [random.expovariate(1/0.5) for n in range(1000)]
    elif f ==  'gammavariate':
        return [random.gammavariate(4, 7) for n in range(1000)]
    elif f ==  'gauss':
        return [random.gauss(1, 0.2) for n in range(1000)]
    elif f ==  'gauss':
        return [random.gauss(1, 0.2) for n in range(1000)]
    elif f ==  'lognormvariate':
        return [random.lognormvariate(1, 0.2) for n in range(1000)]
    elif f ==  'normalvariate':
        return [random.normalvariate(1, 0.2) for n in range(1000)]
    elif f ==  'vonmisesvariate':
        return [random.vonmisesvariate(math.pi/2, 5) for n in range(1000)]
    elif f ==  'paretovariate':
        return [random.paretovariate(100) for n in range(1000)]
    elif f ==  'weibullvariate':
        return [random.weibullvariate(4, 2) for n in range(1000)]

def make_graph(x, func):
    """ヒストグラムを描画"""
    num_bins = 50
    
    fig, ax = plt.subplots()

    ax.set_xlabel('x')
    ax.set_ylabel('Counts')
    ax.set_title(f'Histgram for {func}')
    
    # 正規分布の時は正規化。理論曲線と合わせるため
    if func == "normalvariate":
        n, bins, patches = ax.hist(x, num_bins, density=1) 

        mu = 1
        sigma = 0.2
        y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
        ax.plot(bins, y, '--')
    elif func == 'lognormvariate':
        # xを自然対数に変換
        n, bins, patches = ax.hist(np.log(x), num_bins)
        ax.set_xlabel('ln(x)')

    else:
        # 正規分布以外は、生値でプロット
        n, bins, patches = ax.hist(x, num_bins) 

    fig.tight_layout()
    plt.savefig('./img/' + func + '.png')
    plt.pause(1)
   
def main():
    for d in random_list:
        # randamデータを生成
        x = generate_random_number(d)
        make_graph(x, d)

if __name__ == "__main__":
    main()
