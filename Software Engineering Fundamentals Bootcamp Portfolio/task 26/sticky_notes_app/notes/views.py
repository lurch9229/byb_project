from django.shortcuts import render, redirect, get_object_or_404
from .models import StickyNote
from .forms import StickyNoteForm
from django.http import JsonResponse


# View to display all sticky notes and handle visibility toggle
def index(request):
    notes = StickyNote.objects.all()  # Retrieve all sticky notes
    if request.method == 'POST':
        note_id = request.POST.get('note_id')  # Get the note ID from the POST
        note = get_object_or_404(StickyNote, pk=note_id)
        note.is_visible = not note.is_visible
        note.save()
        return redirect('index')  # Redirect to the index page

    context = {
        'notes': notes,
        'form': StickyNoteForm(),  # Provide an empty form for adding new notes
    }
    return render(request, 'notes/index.html', context)  # Render the index template with the context


# View to toggle the visibility of a specific note
def toggle_note(request, note_id):
    note = get_object_or_404(StickyNote, id=note_id)
    note.is_visible = not note.is_visible  # Toggle the visibility of the note
    note.save()
    return redirect('index')


# View to add a new sticky note
def add_note(request):
    if request.method == 'POST':
        form = StickyNoteForm(request.POST)  # Bind the form with POST data
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StickyNoteForm()  # Provide an empty form if the request is not POST
    return render(request, 'notes/add_note.html', {'form': form})  # Render the add_note template with the form


# Alternative view to add a new sticky note using raw POST data
def add_note_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        StickyNote.objects.create(title=title, description=description)  # Create a new note with the provided data
        return redirect('index')
    return render(request, 'notes/add_note.html')  # Render the add_note template


# View to edit an existing note
def edit_note(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    form = StickyNoteForm(instance=note)  # Provide a form pre-filled with the note's data
    return render(request, 'notes/update_note.html', {'form': form, 'note': note})  # Render the update_note template with the form and note


# View to update an existing sticky note
def update_note(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == 'POST':
        form = StickyNoteForm(request.POST, instance=note)  # Bind the form with POST data and the note instance
        if form.is_valid():
            form.save()  # Save the updated note if the form is valid
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = StickyNoteForm(instance=note)  # Provide a form pre-filled with the note's data
        return render(request, 'notes/update_note.html', {'form': form})  # Render the update_note template with the form


# View to display the details of a specific sticky note
def note_detail_view(request, note_id):
    note = get_object_or_404(StickyNote, id=note_id)
    return render(request, 'notes/note_detail.html', {'note': note})  # Render the note_detail template with the note


# View to delete a specific sticky note
def delete_note(request, note_id):
    note = get_object_or_404(StickyNote, id=note_id)
    if request.method == 'POST':  # Delete the note if the request is POST
        note.delete()
        return redirect('index')
    return render(request, 'notes/delete_note.html', {'note': note})  # Render the delete_note template with the note
