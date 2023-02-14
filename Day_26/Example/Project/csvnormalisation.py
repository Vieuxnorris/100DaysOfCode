import pandas as pd


class CsvNormalisation:

    def __init__(self):
        self.dataFrame = pd.read_csv(filepath_or_buffer="50_states.csv")
        self.listState = self.dataFrame['state'].to_list()
        self.score = 50
        self.stateXY = []
        self.bufferAnswer = []
        self.bufferEnd = []

    def correctAnswer(self, arg_answer):
        if arg_answer in self.listState and arg_answer not in self.bufferAnswer:
            normalisation = self.dataFrame[self.dataFrame['state'] == arg_answer]
            self.bufferAnswer.append(arg_answer)
            self.stateXY = normalisation['state'].to_list() + normalisation['x'].to_list() + \
                           normalisation['y'].to_list()
            self.score -= 1
            return True
        return False

    def returnFullInfos(self):
        return self.stateXY

    def returnEndGame(self):
        self.bufferEnd = [state for state in self.listState if state not in self.bufferAnswer]
        dataEnd = pd.DataFrame(self.bufferEnd)
        dataEnd.to_csv("endDataGame.csv")
        return True
