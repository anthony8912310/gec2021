import sys
def check(word):
    sum = 0
    for c in word:
        sum += ord(c)
    return sum
def insert(word, words):
    len_tmp = check(word)
    for i in range(len(words)):
        len_ori = check(words[i])
        if len_tmp > len_ori:
            words.insert(i, word)
            break

        if i == len(words) - 1 and  len_tmp <= len_ori:
            words.append(word)
if __name__ == '__main__':
    words = []

    n = input()
    for line in sys.stdin.readlines():
        words+=line.rstrip().split(" ")
    
    words.sort(key=len, reverse=True)
    for _ in range(int(n)):
        if not words:
            break

        if len(words)>1:
            i = 0
            if len(words[i]) == len(words[i+1]):
                l1st = []
                l1st.append(words[i])
                l1st.append(words[i+1])

                len1=check(words[i])
                len2=check(words[i+1])

                if len2 > len1:
                    l1st[0], l1st[1] = l1st[1], l1st[0]
                while True:
                    if len(words) >= i+3:
                        if len(words[i+2]) == len(words[i]):
                            insert(words[i+2], l1st)
                            i+=1
                        else:
                            break
                    else:
                        break
                for elem in l1st:
                    print(elem)
                    words.pop(0)
                continue
        print(words[0])
        words.pop(0)
