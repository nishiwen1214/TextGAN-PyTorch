# -*- coding: utf-8 -*-
# @Author       : William
# @Project      : TextGAN-william
# @FileName     : run_exp.py
# @Time         : Created at 2019-07-26
# @Blog         : http://zhiweil.ml/
# @Description  : 
# Copyrights (C) 2018. All Rights Reserved.

import sys
from subprocess import call
import os

# Executables
executable = '/home/zhiwei/.virtualenvs/zhiwei/bin/python'
rootdir = '../'

num_group = 5
run_model = 'evocatgan'
device = 1

ora_pretrain = [0, 1, 1, 1]
gen_pretrain = [0, 1, 1, 1]
loss_type = ['nsgan', 'nsgan', 'nsgan', 'nsgan']
mu_type = ['nsgan', 'nsgan', 'nsgan rsgan', 'nsgan rsgan']
eval_type = ['nll', 'nll', 'nll', 'nll-f1']
ADV_train_epoch = [0, 1500, 1500, 1500]

for i in range(num_group * len(ora_pretrain)):
    job_id = i % len(ora_pretrain)
    args = [
        '--device', device,
        '--run_model', run_model,
        '--ora_pretrain', ora_pretrain[job_id],
        '--gen_pretrain', gen_pretrain[job_id],
        '--loss_type', loss_type[job_id],
        '--mu_type', mu_type[job_id],
        '--eval_type', eval_type[job_id],
        '--adv_epoch', ADV_train_epoch[job_id],
    ]

    args = list(map(str, args))
    my_env = os.environ.copy()
    call([executable, 'main.py'] + args, env=my_env, cwd=rootdir)
