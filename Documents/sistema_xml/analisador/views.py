# analisador/views.py

from django.shortcuts import render
from django.http import HttpResponse
import xml.etree.ElementTree as ET # Biblioteca para processar XML

# Importando nossos modelos (mantemos a referência para uso futuro)
from .models import Empresa, Produto, NotaFiscal, ItemNotaFiscal

def upload_xml(request):
    # Se o formulário foi enviado (método POST)
    if request.method == 'POST':
        # Pegamos o arquivo enviado pelo usuário.
        # Ajustamos o nome para 'xml_file' (o nome original)
        xml_file = request.FILES.get('xml_file')
        
        # Verificamos se um arquivo foi realmente enviado
        if not xml_file:
            return HttpResponse("Nenhum arquivo foi enviado.")
        
        # Verificamos se o arquivo é um XML
        if not xml_file.name.lower().endswith('.xml'):
            return HttpResponse("Por favor, envie um arquivo .xml válido.")

        try:
            # Lógica para ler (parse) o XML.
            # O 'TODO' de salvar os dados no banco ainda está pendente.
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            # Placeholder: Apenas para confirmar que a leitura do XML funcionou
            mensagem_sucesso = f"Arquivo '{xml_file.name}' recebido com sucesso! Elemento raiz: {root.tag}"
            
            return HttpResponse(mensagem_sucesso)

        except ET.ParseError:
            return HttpResponse("Erro ao processar o arquivo XML. Verifique o formato.")
        except Exception as e:
            # Captura outros erros inesperados
            return HttpResponse(f"Ocorreu um erro inesperado: {e}")

    # Se o usuário apenas visitou a página (método GET), mostramos o formulário
    return render(request, 'analisador/upload.html')