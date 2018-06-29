import yaml


if __name__ == '__main__':
    with open('icorpus.yaml') as 檔案:
        chu = yaml.load(檔案)
    m = False
    for pinn in chu:
        if len(pinn['台語']) != len(pinn['華語']):
            print('Tē {} piⁿ Tai-hôa bo peⁿ tn̂g'.format(pinn['文號']))
            m = True
    if m:
        exit(1)
