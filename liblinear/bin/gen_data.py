#!/usr/bin/env python

import argparse, csv, sys, pickle, collections, time

from common import *

features = ["hour", "C1", "banner_pos", "site_id", "site_domain", "site_category", "app_id", "app_domain", "app_category", "device_id", "device_ip", "device_model", "device_type", "device_conn_type", "C14", "C15", "C16", "C17", "C18", "C19", "C20", "C21"]
target = "click"
#FIELDS = ['id','click','hour','banner_pos','site_id','device_id','device_ip','device_model','device_conn_type','C14','C17','C20','C21']
#NEW_FIELDS = FIELDS+['pub_id','pub_domain','pub_category','device_id_count','device_ip_count','user_count','smooth_user_hour_count','user_click_histroy']
max_feature_index = 10000
all_features = []

def fea_hour(f):
    k, v = [], []
    k.append("hh")
    if len(f) == 8:
        v.append(f[6:8])
    else:
        v.append("24")
    return k,v

feature_funcs = {"hour": fea_hour}

start = time.time()
def feature_transform(fe_k, fe_v):
    global feature_funcs
    if fe_k in feature_funcs:
        f = feature_funcs[fe_k]
        k,v = f(fe_v)
    else:
        k,v = [fe_k], [fe_v]
    return k,v

def get_feas_from_orig_data(row):
    global features
    new_row = {}
    for i in features:
        k,v = feature_transform(i, row[i])
        for j in xrange(len(k)):
            new_row[k[j]] = v[j]
    return new_row


def scan(path, show_info = False):
    global max_feature_index, all_features
    count_dict = {}
    for i, row in enumerate(csv.DictReader(open(path)), start=1):
        if i % 100000 == 0:
            sys.stderr.write('{0:6.0f} seconds, read {1} lines.\n'.format(time.time()-start,i ))

        user = def_user(row)
        new_row = get_feas_from_orig_data(row)

        for k in new_row.iterkeys(): # iter feature list
            if k not in count_dict:
                count_dict[k] = {}
            v = new_row[k]
            if v not in count_dict[k]: # value count
                count_dict[k][v] = 0
            count_dict[k][v] += 1

    all_features = new_row.keys()
    if show_info:
        for k1 in count_dict.iterkeys():
            print k1, len(count_dict[k1])

    index_sum = 1
    one_hot_index = {}
    for f in all_features:  # assign one hot index
        for v in count_dict[f].iterkeys():
            one_hot_key = "%s-%s" % (f,v)
            #print one_hot_key, "index: ", index_sum
            one_hot_index[one_hot_key] = index_sum
            index_sum += 1
    max_feature_index = index_sum + 1
    return one_hot_index
        

#history = collections.defaultdict(lambda: {'history': '', 'buffer': '', 'prev_hour': ''})

def gen_data(src_path, dst_path, one_hot_index, is_train = True):
    global max_feature_index, all_features, target
    reader = csv.DictReader(open(src_path))
    writer_all = csv.DictWriter(open(dst_path, 'w'), ["id", target] + all_features, delimiter=' ')

    writer_all.writeheader()

    for i, row in enumerate(reader, start=1):
        if i % 100000 == 0:
            sys.stderr.write('{0:6.0f} seconds write {1} lines\n'.format(time.time()-start,int(i)))
        
        new_row = get_feas_from_orig_data(row)
        for i in all_features:
            k = "%s-%s" % (i, new_row[i])
            if not is_train and k not in one_hot_index:
                new_row[i] = max_feature_index
                print "not found feaure:", k
            else:
                new_row[i] = one_hot_index[k]
        user = def_user(row)
        #new_row['user_id'] = one_hot_index["user_id-%s" % user] 
        new_row['click'] = row["click"] 
        new_row['id'] = row["id"] 

        writer_all.writerow(new_row)

if __name__ == "__main__":
    train_path = sys.argv[1]
    va_path = sys.argv[2]
    train_out = sys.argv[3]
    va_out = sys.argv[4]

    d = scan(train_path, show_info = True)

    print('======================scan complete======================')

    gen_data(va_path, va_out, d, False)
    gen_data(train_path, train_out, d, True)
