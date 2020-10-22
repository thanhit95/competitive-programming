# by Nguyen Trung Thanh       https://www.facebook.com/thanh.it95


K = int(input())

# groupPower = log2(K + 1)
groupPower = (K + 1).bit_length() - 1

positionInGroup = K - ((1 << groupPower) - 1)

resBin = bin(positionInGroup)[2:]
resBin = resBin.rjust(groupPower, '0')

res = resBin.replace('0', '3').replace('1', '5')

print(res)
