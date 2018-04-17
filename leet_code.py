
##############################
# 1. two sum
#############################
def two_sum(arr, target):
    if len(arr) < 2:
        return (-1, -1)
    index_d = {}
    for i,x in enumerate(arr):
        index_d[x] = i
    for i,x in enumerate(arr):
        y = target - x
        if y in index_d:
            return (i, index_d[y])
    return (-1,-1)

def test_two_sum():
    print two_sum([3,3,4,5,6], 6)
    print two_sum([3,3,4,5,6], 7)
    print two_sum([3,3,4,5,6], 8)
    print two_sum([3,3,4,5,6], 9)
    print two_sum([3,3,4,5,6], 11)
    print two_sum([3,3,4,5,6], 181)
    print two_sum([3], 11)

############################
# 2. add two number
############################
class NumberNode:
    def __init__(self, v):
        if type(v) == type(1) and v >= 0 and v <= 9:
            self.value = v
        else:
            raise ValueError("value must between 0 and 9")
        self.next = None
        self.tail = self
    def add_node(self, v):
        if type(v) == type(1) and v >= 0 and v <= 9:
            n = NumberNode(v)
            self.tail.next = n
            self.tail = self.tail.next
        elif type(v) == type([]):
            for i in v:
                if type(i) == type(1) and i >= 0 and i <= 9:
                    n = NumberNode(i)
                    self.tail.next = n
                    self.tail = self.tail.next
        else:
            pass
    def print_node(self):
        n = self.next
        out = "%d" % self.value
        while n is not None:
            out = "%d%s" % (n.value, out)
            n = n.next
        print out 


def add_two_number(n1, n2):
    n3 = None
    carry = 0
    while n1 is not None or n2 is not None or carry > 0 :
        v = carry
        carry = 0
        if n1 is not None:
            v += n1.value
            n1 = n1.next
        if n2 is not None:
            v += n2.value
            n2 = n2.next
        if v >= 10:
            carry = 1
            v = v % 10
        if n3 is None:
            n3 = NumberNode(v)
        else:
            n3.add_node(v)
    return n3

def test_add_two_number():
    n1 = NumberNode(2)
    n2 = NumberNode(5)
    n1.add_node(4)
    n2.add_node(6)
    n1.add_node(3)
    n2.add_node(4)
    n1.print_node()
    n2.print_node()
    
    n3 = add_two_number(n1, n2)
    n3.print_node()

    print "#############"
    n1 = NumberNode(2)
    n2 = NumberNode(5)
    n1.add_node([4,3,9,9,9,9,9,9,9,9,9])
    n2.add_node([6,6])
    n1.print_node()
    n2.print_node()
    
    n3 = add_two_number(n1, n2)
    n3.print_node()

############################
# 5. longest palindromic substring
############################

def longest_pali_str(str_in):
    if len(str_in) <= 1:
        return (-1, "")
    str_l = len(str_in)
    max_l = 1
    max_i = 0
    max_j = 1
    i = 0
    while i < str_l:
        if i < max_l / 2 +1 or (str_l - i) < max_l / 2 + 1:
            i += 1
            continue
        j = i + 1
        # find same char
        while str_in[i] == str_in[j]:
            j += 1
        j -= 1
        # find palindromic string
        k = 1
        while i >= k and j + k < str_l and str_in[i-k] == str_in[j + k]:
            print i,j,k,str_l
            k += 1
        k -= 1
        cur_l = (j + k) - (i - k)+ 1
        if cur_l > max_l:
            max_l = cur_l
            max_i = i - k
            max_j = j + k
        i = j + 1

    return (max_i, str_in[max_i: max_j+ 1])

def testlongest_pali_str():
    print "sldddj"
    print longest_pali_str("slddddddlsj")

############################
# 6. zigzag conversion
############################
def zigzag2(str_in, nrows):
    if len(str_in) <= 1 or nrows == 1:
        return str_in
    l = len(str_in)
    prow = 1
    crow = 1
    n = 0
    out = ""
    crow_incre = 1
    while True:
        
        if crow == prow:
            out += str_in[n]
        n += 1
        crow += crow_incre
        if crow > nrows:
            crow -= 2
            crow_incre = -1
        if crow == 0:
            crow = 2
            crow_incre = 1
        if n >= l:
            n = 0
            prow += 1
            crow = 1
            crow_incre = 1
        if prow > nrows :
            break

    return out

def zigzag(str_in, nrows):
    if len(str_in) <= 1 or nrows == 1:
        return str_in
    l = len(str_in)
    outlist = [""] * nrows 
    crow = 1
    n = 0
    out = ""
    crow_incre = 1
    while True:
        outlist[crow - 1] += str_in[n]
        n += 1
        crow += crow_incre
        if crow > nrows:
            crow -= 2
            crow_incre = -1
        if crow == 0:
            crow = 2
            crow_incre = 1
        if n >= l:
            break
    out = ""
    for i in outlist:
        out += i

    return out


def test_zigzag():
    print "paypalishiring"
    print  zigzag("paypalishiring", 3)

    print "paypalishiring"
    print  zigzag("paypalishiring", 4)

    


if __name__ == "__main__":
    #test_two_sum()

    #test_add_two_number()
    #test_zigzag() 
    testlongest_pali_str()

