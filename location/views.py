from django.shortcuts import render

from location.models import State, LGA
# Create your views here.


def location(request):
    states = State.objects.all()
    state_dict = {}

    for state in states:
        state_dict[state] = state.lga_set.all().count()

        print(state)
        print(state.lga_set.all().count())

    print(state_dict)

    context = {
        'states': states,

    }
    return render(request, 'location/states.html', context)