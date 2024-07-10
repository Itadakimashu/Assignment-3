from django.shortcuts import render
import datetime
def homepage(request):
    data = {
        "current_date": datetime.datetime.now(),
        "students": [
            {'id': '001', 'name': 'Alice Brown', 'hobbies': ['Reading', 'Swimming', 'Gaming']},
            {'id': '002', 'name': 'Bob White', 'hobbies': []},
            {'id': '003', 'name': 'Charlie Green', 'hobbies': ['Cycling', 'Photography']},
            {'id': '004', 'name': 'Daisy Blue', 'hobbies': ['Cooking', 'Traveling', 'Music', 'Drawing']},
            {'id': '005', 'name': 'Evan Yellow', 'hobbies': ['Music', 'Art']},
            {'id': '006', 'name': 'Fiona Red', 'hobbies': ['Running', 'Swimming', 'Gaming', 'Reading']},
        ]
    }
    return render(request,'index.html' , data)