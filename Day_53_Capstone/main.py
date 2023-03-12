from zillowBot import ZyllowBot
from autoGoogleForm import AutoGoogleForm

bot = ZyllowBot()
bot.research(city="san-francisco-ca")
bot.processSoup()

googleForm = AutoGoogleForm()
googleForm.processAuto(bot)
