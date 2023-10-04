from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def start_conversation(request, philosopher):
    # Obtener el usuario actual
    user = request.user

    # Crear una nueva conversación
    conversation = Conversation.objects.create(
        user=user,
        philosopher=philosopher,
    )

    # Obtener la pregunta del usuario
    question = request.POST['question']

    # Generar una respuesta con la API de ChatGPT
    response = chat_gpt.generate_response(question)

    # Guardar la respuesta
    Response.objects.create(
        question=question,
        response=response,
        conversation=conversation,
    )

    # Redirigir al usuario a la página de la conversación
    return HttpResponseRedirect(conversation.get_absolute_url())
