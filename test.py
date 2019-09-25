import main

userInfoFile = open("main_userInfo.json")
diffusionInfoFile = open("main_diffusionInfo.json")
outputFile = open("output.json","w")
outputFile.write(main.main(userInfoFile.read(),diffusionInfoFile.read()))