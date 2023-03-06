from spear.models import Question
from spear.serializer import SpearSerializer


def retriever(index):
    data = Question.objects.get(pk = index)
    print(data)
    serializer = SpearSerializer(data, many=True)
    return JsonResponse({'question': serializer.data})


retriever(1)

