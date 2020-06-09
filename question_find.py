import spacy
import jsonlines
nlp = spacy.load('en_core_web_lg')

def SimilarityFinder(text):
        message = nlp(text)
        answer = dict()
        choices = dict()
        answerkey = dict()
        with jsonlines.open('dataset/dev.jsonl') as reader:
            
            print("entered in json")
            for obj in reader:
                test = nlp(obj['question']['stem']).similarity(message) 
                if(test > 0.75):
                    answer[obj['id']] = obj['answerKey']
                    choices[obj['id']] = {"choices": obj['question']['choices'], "combinedfact":obj['combinedfact']}
                    answerkey[obj['id']]= test
            print("exit from json")

        sort_ans = sorted(answerkey.items(), key = lambda x: x[1], reverse=True)
        id = sort_ans[0][0]
        key= answer[id]
        fa = ""
        for i in choices[id]['choices']:
            if i['label'] == key :
                fa = i['text'].title()
                break
        fa = fa + "\t(FACT: " + choices[id]['combinedfact'].capitalize() +")"
        print(fa) 

        return fa  