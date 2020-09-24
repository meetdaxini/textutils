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
    # get user input
    text = request.POST.get('input', '')
    pr = request.POST.get('pr', 'off')
    cnt = request.POST.get('cnt', 'off')
    nlr = request.POST.get('nlr', 'off')
    sr = request.POST.get('sr', 'off')
    case = request.POST.get('case', 'off')

    analyze = text
    ogCnt = 'Your Original Text is ' + \
        str(charCount(text)) + ' Characters Long.'
    anCnt = ''
    # if elif's to analyze text based on user input considering evry case possible
    # single option selected and case is default
    if pr == 'on' and nlr == 'off' and sr == 'off' and cnt == 'off' and case == 'd':
        analyze = puncRemove(text)
    elif pr == 'off' and nlr == 'on' and sr == 'off' and cnt == 'off' and case == 'd':
        analyze = removeNewLine(text)
    elif pr == 'off' and nlr == 'off' and sr == 'on' and cnt == 'off' and case == 'd':
        analyze = removeSpace(text)
    elif pr == 'off' and nlr == 'off' and sr == 'off' and cnt == 'on' and case == 'd':
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
    # single option selected and case is lower
    elif pr == 'on' and nlr == 'off' and sr == 'off' and cnt == 'off' and case == 'u':
        analyze = lowerCase(analyze)
        analyze = puncRemove(analyze)
    elif pr == 'off' and nlr == 'on' and sr == 'off' and cnt == 'off' and case == 'u':
        analyze = lowerCase(analyze)
        analyze = removeNewLine(analyze)
    elif pr == 'off' and nlr == 'off' and sr == 'on' and cnt == 'off' and case == 'u':
        analyze = lowerCase(analyze)
        analyze = removeSpace(analyze)
    elif pr == 'off' and nlr == 'off' and sr == 'off' and cnt == 'on' and case == 'u':
        analyze = lowerCase(analyze)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
    # single option selected and case is upper
    elif pr == 'on' and nlr == 'off' and sr == 'off' and cnt == 'off' and case == 'u':
        analyze = upperCase(analyze)
        analyze = puncRemove(analyze)
    elif pr == 'off' and nlr == 'on' and sr == 'off' and cnt == 'off' and case == 'u':
        analyze = upperCase(analyze)
        analyze = removeNewLine(analyze)
    elif pr == 'off' and nlr == 'off' and sr == 'on' and cnt == 'off' and case == 'u':

        analyze = upperCase(analyze)
        analyze = removeSpace(analyze)
    elif pr == 'off' and nlr == 'off' and sr == 'off' and cnt == 'on' and case == 'u':
        analyze = upperCase(analyze)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
    # only upper case lowercase default
    elif pr == 'off' and nlr == 'off' and sr == 'off' and cnt == 'off' and case == 'l':
        analyze = lowerCase(text)
    elif pr == 'off' and nlr == 'off' and sr == 'off' and cnt == 'off' and case == 'u':
        analyze = upperCase(text)
    elif pr == 'off' and nlr == 'off' and sr == 'off' and cnt == 'off' and case == 'd':
        pass
    # two switch case one is cnt plus default case
    elif pr == 'off' and nlr == 'off' and sr == 'on' and cnt == 'on' and case == 'd':
        analyze = removeSpace(text)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
    elif pr == 'off' and nlr == 'on' and sr == 'off' and cnt == 'on' and case == 'd':
        analyze = removeNewLine(text)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
    elif pr == 'on' and nlr == 'off' and sr == 'off' and cnt == 'on' and case == 'd':
        analyze = puncRemove(text)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
    # two switch case one is sr plus default case
    elif pr == 'off' and nlr == 'on' and sr == 'on' and cnt == 'off' and case == 'd':
        analyze = removeNewLine(text)
        analyze = removeSpace(analyze)
    elif pr == 'on' and nlr == 'off' and sr == 'on' and cnt == 'off' and case == 'd':
        analyze = puncRemove(text)
        analyze = removeSpace(analyze)
    # two switch case one is nlr plus default case
    elif pr == 'on' and nlr == 'on' and sr == 'off' and cnt == 'off' and case == 'd':
        analyze = puncRemove(text)
        analyze = removeNewLine(analyze)
    # two switch case one is cnt plus upper case
    elif pr == 'off' and nlr == 'off' and sr == 'on' and cnt == 'on' and case == 'u':
        analyze = removeSpace(text)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
        analyze = upperCase(analyze)

    elif pr == 'off' and nlr == 'on' and sr == 'off' and cnt == 'on' and case == 'u':
        analyze = removeNewLine(text)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
        analyze = upperCase(analyze)

    elif pr == 'on' and nlr == 'off' and sr == 'off' and cnt == 'on' and case == 'u':
        analyze = puncRemove(text)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
        analyze = upperCase(analyze)

    # two switch case one is sr plus upper case
    elif pr == 'off' and nlr == 'on' and sr == 'on' and cnt == 'off' and case == 'u':
        analyze = removeNewLine(text)
        analyze = removeSpace(analyze)
        analyze = upperCase(analyze)

    elif pr == 'on' and nlr == 'off' and sr == 'on' and cnt == 'off' and case == 'u':
        analyze = puncRemove(text)
        analyze = removeSpace(analyze)
        analyze = upperCase(analyze)

    # two switch case one is nlr plus upper case
    elif pr == 'on' and nlr == 'on' and sr == 'off' and cnt == 'off' and case == 'u':
        analyze = puncRemove(text)
        analyze = removeNewLine(analyze)
        analyze = upperCase(analyze)
    # two switch case one is cnt plus lower case
    elif pr == 'off' and nlr == 'off' and sr == 'on' and cnt == 'on' and case == 'l':
        analyze = removeSpace(text)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
        analyze = lowerCase(analyze)
    elif pr == 'off' and nlr == 'on' and sr == 'off' and cnt == 'on' and case == 'l':
        analyze = removeNewLine(text)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
        analyze = lowerCase(analyze)

    elif pr == 'on' and nlr == 'off' and sr == 'off' and cnt == 'on' and case == 'l':
        analyze = puncRemove(text)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
        analyze = lowerCase(analyze)
    # two switch case one is sr plus lower case
    elif pr == 'off' and nlr == 'on' and sr == 'on' and cnt == 'off' and case == 'l':
        analyze = removeNewLine(text)
        analyze = removeSpace(analyze)
        analyze = lowerCase(analyze)

    elif pr == 'on' and nlr == 'off' and sr == 'on' and cnt == 'off' and case == 'l':
        analyze = puncRemove(text)
        analyze = removeSpace(analyze)
        analyze = lowerCase(analyze)

    # two switch case one is nlr plus lower case
    elif pr == 'on' and nlr == 'on' and sr == 'off' and cnt == 'off' and case == 'l':
        analyze = puncRemove(text)
        analyze = removeNewLine(analyze)
        analyze = lowerCase(analyze)
    # three switch case plus default case
    elif pr == 'off' and nlr == 'on' and sr == 'on' and cnt == 'on' and case == 'd':
        analyze = removeSpace(text)
        analyze = removeNewLine(analyze)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
    elif pr == 'on' and nlr == 'on' and sr == 'off' and cnt == 'on' and case == 'd':
        analyze = removeNewLine(text)
        analyze = puncRemove(analyze)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
    elif pr == 'on' and nlr == 'off' and sr == 'on' and cnt == 'on' and case == 'd':
        analyze = puncRemove(analyze)
        analyze = removeSpace(analyze)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
    elif pr == 'on' and nlr == 'on' and sr == 'on' and cnt == 'off' and case == 'd':
        analyze = puncRemove(text)
        analyze = removeSpace(analyze)
        analyze = removeNewLine(analyze)
    # three switch case plus upper case
    elif pr == 'off' and nlr == 'on' and sr == 'on' and cnt == 'on' and case == 'u':
        analyze = removeSpace(text)
        analyze = removeNewLine(analyze)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
        analyze = upperCase(analyze)
    elif pr == 'on' and nlr == 'on' and sr == 'off' and cnt == 'on' and case == 'u':
        analyze = removeNewLine(analyze)
        analyze = puncRemove(analyze)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
        analyze = upperCase(analyze)
    elif pr == 'on' and nlr == 'off' and sr == 'on' and cnt == 'on' and case == 'u':
        analyze = puncRemove(analyze)
        analyze = removeSpace(analyze)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
        analyze = upperCase(analyze)
    elif pr == 'on' and nlr == 'on' and sr == 'on' and cnt == 'off' and case == 'u':
        analyze = puncRemove(analyze)
        analyze = removeSpace(analyze)
        analyze = removeNewLine(analyze)
        analyze = upperCase(analyze)
    # three switch case plus lower case
    elif pr == 'off' and nlr == 'on' and sr == 'on' and cnt == 'on' and case == 'l':
        analyze = removeSpace(text)
        analyze = removeNewLine(analyze)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
        analyze = lowerCase(analyze)
    elif pr == 'on' and nlr == 'on' and sr == 'off' and cnt == 'on' and case == 'l':
        analyze = removeNewLine(text)
        analyze = puncRemove(analyze)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
        analyze = lowerCase(analyze)
    elif pr == 'on' and nlr == 'off' and sr == 'on' and cnt == 'on' and case == 'l':
        analyze = puncRemove(analyze)
        analyze = removeSpace(analyze)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
        analyze = lowerCase(analyze)
    elif pr == 'on' and nlr == 'on' and sr == 'on' and cnt == 'off' and case == 'l':
        analyze = puncRemove(text)
        analyze = removeSpace(analyze)
        analyze = removeNewLine(analyze)
        analyze = lowerCase(analyze)
    # four switch i.e all plus default or upper or lower
    elif pr == 'on' and nlr == 'on' and sr == 'on' and cnt == 'on' and case == 'l':
        analyze = puncRemove(analyze)
        analyze = removeSpace(analyze)
        analyze = removeNewLine(analyze)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
        analyze = lowerCase(analyze)
    elif pr == 'on' and nlr == 'on' and sr == 'on' and cnt == 'on' and case == 'u':
        analyze = puncRemove(analyze)
        analyze = removeSpace(analyze)
        analyze = removeNewLine(analyze)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
        analyze = upperCase(analyze)
    elif pr == 'on' and nlr == 'on' and sr == 'on' and cnt == 'on' and case == 'd':
        analyze = puncRemove(analyze)
        analyze = removeSpace(analyze)
        analyze = removeNewLine(analyze)
        anCnt = 'Your Analyzed Text is ' + \
            str(charCount(analyze)) + ' Characters Long.'
    else:
        analyze = 'error'
    params = {"anText": analyze, "ogText": text,
              'anCnt': anCnt, 'ogCnt': ogCnt}
    return render(request, 'analyzed.html', params)
