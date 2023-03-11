from internetSpeedTwitterBot import InternetSpeedTwitterBot

botTwitter = InternetSpeedTwitterBot()
speed = botTwitter.getInternetSpeed()
print(f"Down: {speed['down']}\nUp: {speed['up']}")
botTwitter.tweetAtProvider()
