# We have to create this file by ourself.
from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render(request, 'index.html')


def charCount(text):
    return len(text)


def removeSpace(text):
    remS = ''
    for ch in text:
        if ch != ' ':
            remS += ch
    return remS


def removeNewLine(text):
    remN = ''
    for ch in text:
        if ch != '\n' and ch != '\r':
            remN += ch
    print(remN)
    return remN


def upperCase(text):
    return text.upper()


def lowerCase(text):
    return text.lower()


def puncRemove(text):
    punc_Free = ''
    for chr in text:
        if chr not in string.punctuation:
            punc_Free += chr
    return punc_Free


def features(request):
    return render(request, "features.html")


def tutorials(request):
    return render(request, "tutorials.html")

def analyzed(request):
    text = request.POST.get('input', '')
    pr = request.POST.get('pr', 'off')
    cnt = request.POST.get('cnt', 'off')
    nlr = request.POST.get('nlr', 'off')
    sr = request.POST.get('sr', 'off')
    case = request.POST.get('case', 'off')

    analyze = text
    ogCnt = 'Your Original Text is ' + str(charCount(text)) + ' Characters Long.'
    anCnt = ''

    if pr == 'on' and nlr == 'off' and sr == 'off' and cnt == 'off' and case == 'd':
        analyze = puncRemove(text)
    elif pr == 'off' and nlr == 'on' and sr == 'off' and cnt == 'off' and case == 'd':
        analyze = removeNewLine(text)
    elif pr == 'off' and nlr == 'off' and sr == 'on' and cnt == 'off' and case == 'd':
        analyze = removeSpace(text)
    elif pr == 'off' and nlr == 'off' and sr == 'off' and cnt == 'on' and case == 'd':
        anCnt = 'Your Analyzed Text is ' + str(charCount(text)) + ' Characters Long.'
    elif pr == 'off' and nlr == 'off' and sr == 'off' and cnt == 'off' and case == 'l':
        analyze = lowerCase(text)
    elif pr == 'off' and nlr == 'off' and sr == 'off' and cnt == 'off' and case == 'u':
        analyze = upperCase(text)
    elif pr == 'off' and nlr == 'off' and sr == 'off' and cnt == 'off' and case == 'd':
        analyze = text
    elif pr == 'off' and nlr == 'off' and sr == 'on' and cnt == 'on' and case == 'd':
        analyze = removeSpace(text)
        anCnt = 'Your Analyzed Text is ' + str(charCount(analyze)) + ' Characters Long.'
    elif pr == 'on' and nlr == 'off' and sr == 'off' and cnt == 'off' and case == 'u':
        analyze = upperCase(text)
        analyze = puncRemove(analyze)


    else:
        analyze = 'else'
    params = {"anText": analyze, "ogText": text, 'anCnt': anCnt, 'ogCnt': ogCnt}
    return render(request, 'analyzed.html', params)
