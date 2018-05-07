#!/usr/bin/env python

import sys
import random


if __name__ == "__main__":
    va_ratio = int(sys.argv[1])
    train_data = sys.argv[2]
    train_data_out = sys.argv[3]
    va_data_out = sys.argv[4]
    va_data_prefix = "va"

    va_file = open(va_data_out, 'w')
    train_file = open(train_data_out,'w')

    with open(train_data, 'r') as f, open(va_data_out, 'w') as v, open(train_data_out,'w') as t:
        for l in f:
            r = random.randint(1,100)
            if r < va_ratio:
                v.write(l)
            else:
                t.write(l)




        

    

