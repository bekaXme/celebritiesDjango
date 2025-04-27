from django.shortcuts import render

# Fake database
CELEBRITIES = [
    {
        'id': 1,
        'name': 'Elon Musk',
        'profession': 'Entrepreneur',
        'bio': 'Founder of SpaceX and Tesla.',
        'image': 'celebrities/images/elon_musk.jpg'
    },
    {
        'id': 2,
        'name': 'Taylor Swift',
        'profession': 'Singer',
        'bio': 'Famous American singer and songwriter.',
        'image': 'celebrities/images/taylor_swift.jpg'
    },
]

def home(request):
    context = {
        'celebrities': CELEBRITIES,
        'title': 'Mashhur Shaxslar Galereyasi'
    }
    return render(request, 'celebrities/home.html', context)

def detail(request, celebrity_id):
    celebrity = next((c for c in CELEBRITIES if c['id'] == celebrity_id), None)
    if celebrity is None:
        return render(request, '404.html', status=404)
    context = {
        'celebrity': celebrity,
        'title': celebrity['name']
    }
    return render(request, 'celebrities/detail.html', context)
