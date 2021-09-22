jyus=input('住所を入力してください:')
target = '都'
target2 = '道'
target3 = '府'
target4 = '県'
if jyus.count('都') == 1:
    print(jyus[jyus.find(target) + 1:])
elif jyus.count('道') == 1:
    print(jyus[jyus.find(target2) + 1:])
elif jyus.count('府') == 1:
    print(jyus[jyus.find(target3) + 1:])
elif jyus.count('県') == 1:
    print(jyus[jyus.find(target4)+1:])
 