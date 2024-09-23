import PyPDF2
import nltk
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser
from .models import ExtractedData
from django.shortcuts import render

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

def upload_view(request):
    return render(request, 'upload.html')

class UploadPDFView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.data['file']
        email = request.data['email']
        reader = PyPDF2.PdfReader(file)
        text = ' '.join(page.extract_text() for page in reader.pages)
        tokens = nltk.word_tokenize(text)
        nouns = [word for word, pos in nltk.pos_tag(tokens) if pos.startswith('NN')]
        verbs = [word for word, pos in nltk.pos_tag(tokens) if pos.startswith('VB')]

        extracted_data = ExtractedData(email=email, nouns=nouns, verbs=verbs)
        extracted_data.save()

        return Response({"email": email, "nouns": nouns, "verbs": verbs}, status=status.HTTP_201_CREATED)