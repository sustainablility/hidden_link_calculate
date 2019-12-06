from constructR import *
from matchingPersuit import *
from main import *

userInfoRead = open('./main_userInfo_records.json')
diffusionInfoRead = open('./main_diffusionInfo_records.json')

mainout = main(userInfoRead.read(),diffusionInfoRead.read())

rout = parallel_r_main(mainout)
miniout = parallel_minimizer(rout)
print(miniout)