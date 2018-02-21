from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import webhoseio


def index(request):
    # Create your views here.
    webhoseio.config(token="8ebd85ed-94da-4ae1-9bd2-def0554ceb64")
    query_params = {
    "q": "(site:bloomberg.com OR site:reuters.com) AND ('mapletree' OR 'capitaland' OR 'Keppel')",
    "ts": "1516541338427",
    "sort": "published"
    }
    output = webhoseio.query("filterWebContent", query_params)
    context = {'output': output}
    return render(request, 'news/index.html', context)

# def index(request):
#     # Create your views here.
#     webhoseio.config(token="8ebd85ed-94da-4ae1-9bd2-def0554ceb64")
#     query_params = {
#     "q": "(site:bloomberg.com OR site:reuters.com) AND ('mapletree' OR 'capitaland' OR 'Keppel' OR 'AIMS AMP Capital' OR 'Sabana REIT')",
#     "ts": "1516537944411",
#     "sort": "crawled"
#     }
#     output = webhoseio.query("filterWebContent", query_params)
#     return JsonResponse(output)