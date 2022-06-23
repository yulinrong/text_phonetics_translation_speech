import fileinput
import eng_to_ipa as p 
import pyttsx3
import re
import html
from urllib import parse
import requests

GOOGLE_TRANSLATE_URL = 'http://translate.google.cn/m?q=%s&tl=%s&sl=%s'
def translate(text, to_language="auto", text_language="auto"):
    text = parse.quote(text)
    url = GOOGLE_TRANSLATE_URL % (text,to_language,text_language)
    response = requests.get(url)
    data = response.text
    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    result = re.findall(expr, data)
    if (len(result) == 0):
        return ""
    return html.unescape(result[0])


if __name__=='__main__':
    print("\033[0;32;40m\tPlease put your sentences in data.txt.\033[0m")
    engine = pyttsx3.init()

    i = 0
    for line in open('data.txt',encoding='utf-8'):
        if line[0] != '-' and line != '\n':
            i += 1
            sentence = re.split(r'[].?]',line)[0]
            phonetics = p.convert(sentence)
            print("\033[0;35;40m\t"+sentence+"\033[0m",'    ',i)
            print("\033[0;37;40m\t"+phonetics+"\033[0m")
            print("\033[0;36;40m\t"+translate(sentence,"zh-CN","en")+"\033[0m")
            engine.say(sentence)
            engine.runAndWait()
            input()
            print('-----------------------------------------------------------Press Enter')

main()