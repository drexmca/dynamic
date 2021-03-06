import ogusa
import os
import sys
from multiprocessing import Process
import time

#OGUSA_PATH = os.environ.get("OGUSA_PATH", "../../ospc-dynamic/dynamic/Python")

#sys.path.append(OGUSA_PATH)

import postprocess
#from execute import runner # change here for small jobs
from execute_large import runner


def run_micro_macro(user_params):

    # reform = {
    # 2015: {
    #     '_II_rt1': [.09],
    #     '_II_rt2': [.135],
    #     '_II_rt3': [.225],
    #     '_II_rt4': [.252],
    #     '_II_rt5': [.297],
    #     '_II_rt6': [.315],
    #     '_II_rt7': [0.3564],
    # }, }

    reform = {
    2015: {
        '_II_rt7': [0.35],
    }, }


    start_time = time.time()

    REFORM_DIR = "./OUTPUT_REFORM"
    BASELINE_DIR = "./OUTPUT_BASELINE"

    output_base = REFORM_DIR
    input_dir = REFORM_DIR

    guid_iter = 'reform_' + str(0)

    
    kwargs={'output_base':output_base, 'input_dir':input_dir,
            'baseline':False, 'analytical_mtrs':True, 'age_specific':False, 
            'reform':reform, 'user_params':user_params,'guid':'99', 'run_micro':True}
    #p2 = Process(target=runner, kwargs=kwargs)
    #p2.start()
    runner(**kwargs)

    output_base = BASELINE_DIR
    input_dir = BASELINE_DIR
    kwargs={'output_base':output_base, 'input_dir':input_dir,
            'baseline':True, 'analytical_mtrs':True, 'age_specific':False,
            'user_params':user_params,'guid':'99',
            'run_micro':True}
    #p1 = Process(target=runner, kwargs=kwargs)
    #p1.start()
    runner(**kwargs)

    #p1.join()
    print "just joined"
    #p2.join()

    time.sleep(0.5)

    ans = postprocess.create_diff(baseline=BASELINE_DIR, policy=REFORM_DIR)

    print "total time was ", (time.time() - start_time)
    print ans

    return ans

if __name__ == "__main__":
    run_micro_macro(user_params={})
