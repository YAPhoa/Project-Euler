def UndThousand(n) :
    Hun = n // 100
    Ten = n % 100
    ends = " " + "Hundred" + " " + UndHundred(Ten)
    if Hun == 1 :
        return "One" + ends
    if Hun == 2 :
        return "Two" + ends
    if Hun == 3 :
        return "Three" + ends
    if Hun == 4 :
        return "Four" + ends
    if Hun == 5 :
        return "Five" + ends
    if Hun == 6 :
        return "Six" + ends
    if Hun == 7 :
        return "Seven" + ends
    if Hun == 8 :
        return "Eight" + ends
    if Hun == 9 :
        return "Nine" + ends
    return UndHundred(n)

def splitz(n) :
    out = []
    while True :
        out.insert(0,n%1000)
        n = n // 1000
        if n == 0 :
            return out
        
def NumtoWords(n) :
    arr = splitz(n)
    final = ""
    for i in range(len(arr)) :
        ps = arr[len(arr)-1-i]
        pros = UndThousand(ps)
        if i == 0 :
            if ps == 0 :
                continue
            final = pros + final
        if i == 1 :
            if ps == 0 :
                continue
            final = pros + " " + "Thousand" + " " + final
        if i == 2 :
            if ps == 0 :
                continue
            else :
                final = pros + " " + "Million" + " " + final
        if i == 3 :
            if ps == 0 :
                continue
            else :
                final = pros + " " + "Billion" + " " + final
        if i == 4 :
            if ps == 0 :
                continue
            else :
                final = pros + " " + "Trillion" + " " + final
        if i == 5 :
            if ps == 0 :
                continue
            else :
                final = pros + " " + "Quadrillion" + " " + final
    return final

def UndHundred(n) :
    if n == 10 :
        return "Ten"
    if n == 11 :
        return "Eleven"
    if n == 12 :
        return "Twelve"
    if n == 13 :
        return "Thirteen"
    if n == 14 :
        return "Fourteen"
    if n == 15 :
        return "Fifteen"
    if n == 16 :
        return "Sixteen"
    if n == 17 :
        return "Seventeen"
    if n == 18 :
        return "Eighteen"
    if n == 19 :
        return "Nineteen"
    Tenth = n // 10
    if Tenth == 2 :
        return "Twenty" + " " + UndTen(n % 10)
    if Tenth == 3 :
        return "Thirty" + " " + UndTen(n % 10)
    if Tenth == 4 :
        return "Forty" + " " + UndTen(n%10)
    if Tenth == 5 :
        return "Fifty" + " " + UndTen(n%10)
    if Tenth == 6 :
        return "Sixty" + " " + UndTen(n%10)
    if Tenth == 7 :
        return "Seventy" + " " + UndTen(n%10)
    if Tenth == 8 :
        return "Eighty"  + " " + UndTen(n%10)
    if Tenth == 9 :
        return "Ninety" + " " + UndTen(n%10)
    return UndTen(n)
    
def UndTen(n) :
    if n == 0 :
        return ""
    if n == 1 :
        return "One"
    if n == 2 :
        return "Two"
    if n == 3 :
        return "Three"
    if n == 4 :
        return "Four"
    if n == 5 :
        return "Five"
    if n == 6 :
        return "Six"
    if n == 7 :
        return "Seven"
    if n == 8 :
        return "Eight"
    if n == 9 :
        return "Nine"
    
k = int(input())

for i in range(k) :
    c = int(input())
    if c == 0 :
        print("Zero")
    else :
        print(NumtoWords(c))

