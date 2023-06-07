import pandas as pd
from levenshtein import distance

"""과제 상세 설명:
1. 학습데이터의 질문과 chat의 질문의 유사도를 레벤슈타인 거리를 이용해 구하기
--> levenshtein.py 파일에 distance함수를 작성하고 불러온다.
2. chat의 질문과 레벤슈타인 거리와 가장 유사한 학습데이터의 질문의 인덱스를 구하기
--> 각 질문들과의 레벤슈타인 길이를 levenshtein_score 배열에 저장. 배열의 최소값의 인덱스
3. 학습 데이터의 인덱스의 답을 chat의 답변을 채택한 뒤 출력
--> 2의 인덱스로부터 답변의 답을 출력
"""


class LevenshteinChatBot:
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)  # 인스턴스 생성 시 'ChatbotData.csv' 파일 불러오기

    def load_data(self, filepath):  # 그대로 사용
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()  # 질문열만 뽑아 파이썬 리스트로 저장
        answers = data['A'].tolist()   # 답변열만 뽑아 파이썬 리스트로 저장
        return questions, answers

    def find_best_answer(self, input_sentence):  # 레벤슈타인 거리를 통해 답을 찾도록 함수 변경
        levenshtein_score = []
        for question in self.questions:  # 데이터의 모든 질문과 사용자 질문 사이의 거리를 배열에 담기
            levenshtein_score.append(distance(question, input_sentence))
        best_match_index = levenshtein_score.index(min(levenshtein_score))   # 레벤슈타인 거리가 짧은 답의 인덱스를 반환
        return self.answers[best_match_index]

# CSV 파일 경로를 지정하세요.
filepath = 'ChatbotData.csv'

# 레벤슈타인 챗봇 인스턴스를 생성합니다.
chatbot = LevenshteinChatBot(filepath)

# '종료'라는 단어가 입력될 때까지 챗봇과의 대화를 반복합니다.
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_best_answer(input_sentence)
    print('Chatbot:', response)
    
