from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
import json
from app.models import Data


def match(pat, txt):
    ''' Naive pattern matching algorithm to match given pattern 
        inside given text. Takes pattern and text as input and 
        returns array containing text and index of pattern occurance 
        if match found else returns None. '''
    
    pat_len = len(pat)
    txt_len = len(txt)
  
    for i in range(txt_len - pat_len + 1): 
        j = 0
        count=0
        for j in range(0, pat_len): 
            if (txt[i + j] != pat[j]):
                count+=1
                break
  
        if (j == pat_len - 1) and count==0:
            return [txt, i]

    return None


def insert_position(index, array):
    ''' Takes index of pattern occurance in text and array
        of pattern positions in text, finds where the new index
        has to be inserted and returns the index '''

    for key, val in enumerate(array):
        if index < val:
            return key

    return len(array)

@require_GET
def search(request):
    ''' Takes GET request with "word" parameter and returns json 
        response containing array of matched words from database '''

    pattern = []
    occurance_idx = []

    word = request.GET.get("word", "")
    if word != "":
        # Get strings that contains the given pattern
        dataset = Data.objects.filter(
            string__contains=word).order_by('-occurance').values_list(
            'string', flat=True)

        # loop through data set and arrange them based on
        # order of occurance, length of the string and number of occurances
        for val in dataset:
            text = match(word, val)
            if text is not None:
                if text[0] == word:
                    # if the pattern and string is a perfect match
                    # insert at beginning of the list
                    pattern.insert(0, text[0])
                    occurance_idx.insert(0, 0)
                else:
                    if len(occurance_idx) == 0:
                        # if the pattern list and ocurance_idx list is empty
                        # append the text and position
                        occurance_idx.append(text[1])
                        pattern.append(text[0])
                    else:
                        # if the list is not empty search for postion
                        # in occurance_idx list and insert the text at 
                        # appropriate index. 
                        index = insert_position(text[1], occurance_idx)
                        occurance_idx.insert(index, text[1])
                        pattern.insert(index, text[0])

            if len(pattern) >= 25:
                break

    return JsonResponse(
        {
            "success": True,
            # sort the pattern_list based on length of strings in pattern list
            "data": sorted(pattern, key=len)
        }
    )
