from django.http import HttpResponse
from django.http import request
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    fullText = request.GET['fulltext']

    wordList = fullText.split()

    word_dictionary = {}

    for word in wordList:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    sorted_word_dictionary = sorted(
        word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", {'fullText': fullText, 'count': len(wordList), 'wordDic': sorted_word_dictionary})
