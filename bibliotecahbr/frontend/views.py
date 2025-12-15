import json
import requests
from urllib.parse import urlencode

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

API_PREFIX = '/api'


def _api_url(request, path, parametros=None):
    scheme = request.scheme
    host = request.get_host()
    url = f"{scheme}://{host}{API_PREFIX}{path}"
    if parametros:
        url = f"{url}?{urlencode(parametros)}"
    return url


def _api_request(request, method, path, dados_json=None, parametros=None):
    url = _api_url(request, path, parametros=parametros)
    try:
        resposta = requests.request(method, url, json=dados_json, timeout=5)
        try:
            dados_resposta = resposta.json()
        except Exception:
            dados_resposta = resposta.text
        return resposta.status_code, dados_resposta
    except requests.RequestException as e:
        return 500, {'detail': str(e)}


def livro_list(request):
    parametros = {}
    titulo = request.GET.get('titulo')
    ano = request.GET.get('ano')
    if titulo:
        parametros['titulo'] = titulo
    if ano:
        parametros['ano'] = ano

    codigo_status, dados_resposta = _api_request(request, 'GET', '/livros/', parametros=parametros if parametros else None)
    livros = dados_resposta if isinstance(dados_resposta, list) else []
    contexto = {'livros': livros, 'errors': None}
    if codigo_status != 200:
        contexto['errors'] = dados_resposta
    return render(request, 'frontend/livro_list.html', contexto)


@require_http_methods(['GET', 'POST'])
def livro_create(request):
    if request.method == 'GET':
        return render(request, 'frontend/livro_form.html', {'form_data': {}, 'errors': None})

    dados_envio = {
        'titulo': request.POST.get('titulo', ''),
        'autor': request.POST.get('autor', ''),
        'ano': int(request.POST.get('ano')) if request.POST.get('ano') else None,
        'isbn': request.POST.get('isbn', ''),
        'disponivel': request.POST.get('disponivel', 'Disponível')
    }
    codigo_status, dados_resposta = _api_request(request, 'POST', '/livros/cadastrar', dados_json=dados_envio)
    if codigo_status in (200, 201):
        return redirect(reverse('frontend:livro_list'))
    return render(request, 'frontend/livro_form.html', {'form_data': dados_envio, 'errors': dados_resposta})


def livro_detail(request, pk):
    codigo_status, dados_resposta = _api_request(request, 'GET', f'/livros/{pk}/')
    if codigo_status != 200:
        return render(request, 'frontend/livro_detail.html', {'livro': None, 'errors': dados_resposta})
    return render(request, 'frontend/livro_detail.html', {'livro': dados_resposta, 'errors': None})


@require_http_methods(['GET', 'POST'])
def livro_edit(request, pk):
    if request.method == 'GET':
        codigo_status, dados_resposta = _api_request(request, 'GET', f'/livros/{pk}/')
        if codigo_status != 200:
            return render(request, 'frontend/livro_form.html', {'form_data': {}, 'errors': dados_resposta})
        return render(request, 'frontend/livro_form.html', {'form_data': dados_resposta, 'errors': None})

    dados_envio = {
        'titulo': request.POST.get('titulo', ''),
        'autor': request.POST.get('autor', ''),
        'ano': int(request.POST.get('ano')) if request.POST.get('ano') else None,
        'isbn': request.POST.get('isbn', ''),
        'disponivel': request.POST.get('disponivel', 'Disponível')
    }
    codigo_status, dados_resposta = _api_request(request, 'PUT', f'/livros/{pk}/', dados_json=dados_envio)
    if codigo_status in (200, 204):
        return redirect(reverse('frontend:livro_detail', args=[pk]))
    return render(request, 'frontend/livro_form.html', {'form_data': dados_envio, 'errors': dados_resposta})


@require_http_methods(['POST'])
def livro_delete(request, pk):
    _api_request(request, 'DELETE', f'/livros/{pk}/')
    return redirect(reverse('frontend:livro_list'))


def menu(request):
    return render(request, 'frontend/menu.html')


def usuario_list(request):
    codigo_status, dados_resposta = _api_request(request, 'GET', '/usuarios/')
    usuarios = dados_resposta if isinstance(dados_resposta, list) else []
    contexto = {'usuarios': usuarios, 'errors': None}
    if codigo_status != 200:
        contexto['errors'] = dados_resposta
    return render(request, 'frontend/usuario_list.html', contexto)


@require_http_methods(['GET', 'POST'])
def usuario_create(request):
    if request.method == 'GET':
        return render(request, 'frontend/usuario_form.html', {'form_data': {}, 'errors': None})

    dados_envio = {
        'nome': request.POST.get('nome', ''),
        'matricula': request.POST.get('matricula', ''),
        'email': request.POST.get('email', ''),
    }
    codigo_status, dados_resposta = _api_request(request, 'POST', '/usuarios/cadastrar', dados_json=dados_envio)
    if codigo_status in (200, 201):
        return redirect(reverse('frontend:usuario_list'))
    return render(request, 'frontend/usuario_form.html', {'form_data': dados_envio, 'errors': dados_resposta})


def usuario_detail(request, pk):
    codigo_status, dados_resposta = _api_request(request, 'GET', f'/usuarios/{pk}/')
    if codigo_status != 200:
        return render(request, 'frontend/usuario_detail.html', {'usuario': None, 'errors': dados_resposta})
    return render(request, 'frontend/usuario_detail.html', {'usuario': dados_resposta, 'errors': None})


@require_http_methods(['GET', 'POST'])
def usuario_edit(request, pk):
    if request.method == 'GET':
        codigo_status, dados_resposta = _api_request(request, 'GET', f'/usuarios/{pk}/')
        if codigo_status != 200:
            return render(request, 'frontend/usuario_form.html', {'form_data': {}, 'errors': dados_resposta})
        return render(request, 'frontend/usuario_form.html', {'form_data': dados_resposta, 'errors': None})

    dados_envio = {
        'nome': request.POST.get('nome', ''),
        'matricula': request.POST.get('matricula', ''),
        'email': request.POST.get('email', ''),
    }
    codigo_status, dados_resposta = _api_request(request, 'PUT', f'/usuarios/{pk}/', dados_json=dados_envio)
    if codigo_status in (200, 204):
        return redirect(reverse('frontend:usuario_detail', args=[pk]))
    return render(request, 'frontend/usuario_form.html', {'form_data': dados_envio, 'errors': dados_resposta})


@require_http_methods(['POST'])
def usuario_delete(request, pk):
    _api_request(request, 'DELETE', f'/usuarios/{pk}/')
    return redirect(reverse('frontend:usuario_list'))


def emprestimo_list(request):
    codigo_status, dados_resposta = _api_request(request, 'GET', '/emprestimos/')
    emprestimos = dados_resposta if isinstance(dados_resposta, list) else []
    contexto = {'emprestimos': emprestimos, 'errors': None}
    if codigo_status != 200:
        contexto['errors'] = dados_resposta
    return render(request, 'frontend/emprestimo_list.html', contexto)


@require_http_methods(['GET', 'POST'])
def emprestimo_create(request):
    if request.method == 'GET':
        # obter usuarios e livros para selects
        codigo_usuarios, usuarios_resposta = _api_request(request, 'GET', '/usuarios/')
        codigo_livros, livros_resposta = _api_request(request, 'GET', '/livros/')
        return render(request, 'frontend/emprestimo_form.html', {'form_data': {}, 'errors': None, 'usuarios': usuarios_resposta or [], 'livros': livros_resposta or []})

    dados_envio = {
        'id_usuario': int(request.POST.get('id_usuario')) if request.POST.get('id_usuario') else None,
        'id_livro': int(request.POST.get('id_livro')) if request.POST.get('id_livro') else None,
        'data_emp': request.POST.get('data_emp') or None,
        'dev_prev': request.POST.get('dev_prev') or None,
    }
    codigo_status, dados_resposta = _api_request(request, 'POST', '/emprestimos/realizar', dados_json=dados_envio)
    if codigo_status in (200, 201):
        return redirect(reverse('frontend:emprestimo_list'))
    # repopular selects
    codigo_usuarios, usuarios_resposta = _api_request(request, 'GET', '/usuarios/')
    codigo_livros, livros_resposta = _api_request(request, 'GET', '/livros/')
    return render(request, 'frontend/emprestimo_form.html', {'form_data': dados_envio, 'errors': dados_resposta, 'usuarios': usuarios_resposta or [], 'livros': livros_resposta or []})


def emprestimo_detail(request, pk):
    codigo_status, dados_resposta = _api_request(request, 'GET', f'/emprestimos/{pk}/')
    if codigo_status != 200:
        return render(request, 'frontend/emprestimo_detail.html', {'emprestimo': None, 'errors': dados_resposta})
    return render(request, 'frontend/emprestimo_detail.html', {'emprestimo': dados_resposta, 'errors': None})


@require_http_methods(['GET', 'POST'])
def emprestimo_edit(request, pk):
    if request.method == 'GET':
        codigo_status, dados_resposta = _api_request(request, 'GET', f'/emprestimos/{pk}/')
        if codigo_status != 200:
            return render(request, 'frontend/emprestimo_form.html', {'form_data': {}, 'errors': dados_resposta, 'usuarios': [], 'livros': []})
        codigo_usuarios, usuarios_resposta = _api_request(request, 'GET', '/usuarios/')
        codigo_livros, livros_resposta = _api_request(request, 'GET', '/livros/')
        return render(request, 'frontend/emprestimo_form.html', {'form_data': dados_resposta, 'errors': None, 'usuarios': usuarios_resposta or [], 'livros': livros_resposta or []})

    dados_envio = {
        'id_usuario': int(request.POST.get('id_usuario')) if request.POST.get('id_usuario') else None,
        'id_livro': int(request.POST.get('id_livro')) if request.POST.get('id_livro') else None,
        'data_emp': request.POST.get('data_emp') or None,
        'dev_prev': request.POST.get('dev_prev') or None,
        'data_dev': request.POST.get('data_dev') or None,
        'status': request.POST.get('status') or None,
    }
    codigo_status, dados_resposta = _api_request(request, 'PUT', f'/emprestimos/{pk}/', dados_json=dados_envio)
    if codigo_status in (200, 204):
        return redirect(reverse('frontend:emprestimo_detail', args=[pk]))
    codigo_usuarios, usuarios_resposta = _api_request(request, 'GET', '/usuarios/')
    codigo_livros, livros_resposta = _api_request(request, 'GET', '/livros/')
    return render(request, 'frontend/emprestimo_form.html', {'form_data': dados_envio, 'errors': dados_resposta, 'usuarios': usuarios_resposta or [], 'livros': livros_resposta or []})


@require_http_methods(['POST'])
def emprestimo_delete(request, pk):
    _api_request(request, 'DELETE', f'/emprestimos/{pk}/')
    return redirect(reverse('frontend:emprestimo_list'))
