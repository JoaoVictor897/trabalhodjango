from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemEstoque
from .forms import NovoItemForm, ItemEstoqueForm


def lista_estoque(request):
    
    itens = ItemEstoque.objects.all()  # Obtém todos os itens do estoque
    return render(request, "estoque/lista_estoque.html", {"itens": itens})


def novo_item(request):
    
    if request.method == "POST":
        form = NovoItemForm(request.POST)  # Cria um formulário com os dados da requisição POST
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva o novo item no banco de dados
            return redirect("lista_estoque")  # Redireciona para a lista de itens
    else:
        form = NovoItemForm()  # Cria um formulário vazio (para ser preenchido pelo usuário)

    return render(request, "estoque/novo_item.html", {"form": form})


def adicionar_item(request):
    
    if request.method == "POST":
        form = NovoItemForm(request.POST)  # Cria um formulário com os dados da requisição POST
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva o novo item no banco de dados
            return redirect("lista_estoque")  # Redireciona para a lista de itens
    else:
        form = NovoItemForm()  # Cria um formulário vazio (para ser preenchido pelo usuário)

    return render(request, "estoque/adicionar_item.html", {"form": form})


def detalhes_item(request, id):
    
    item = get_object_or_404(ItemEstoque, id=id)  # Obtém o item com o ID fornecido
    return render(request, "estoque/detalhes_item.html", {"item": item})


def editar_item(request, id):
    
    item = get_object_or_404(ItemEstoque, id=id)  # Obtém o item com o ID fornecido

    if request.method == "POST":
        form = ItemEstoqueForm(request.POST, instance=item)  # Cria um formulário com os dados da requisição POST
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no item
            return redirect("detalhes_item", id=id)  # Redireciona para a página de detalhes do item
    else:
        form = ItemEstoqueForm(instance=item)  # Cria um formulário preenchido com os dados atuais do item

    return render(request, "estoque/editar_item.html", {"form": form, "item": item})


def confirmar_exclusao_item(request, id):
    
    item = get_object_or_404(ItemEstoque, id=id)  # Obtém o item com o ID fornecido
    return render(request, "estoque/confirmar_exclusao_item.html", {"item": item})


def excluir_item(request, id):
    
    item = get_object_or_404(ItemEstoque, id=id)  # Obtém o item com o ID fornecido
    item.delete()  # Exclui o item do banco de dados
    return redirect("lista_estoque")  # Redireciona para a lista de itens