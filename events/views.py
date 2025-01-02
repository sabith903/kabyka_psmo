from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Result, Category, Department, Schedule, Student, Image

def home(request):
    images = Image.objects.all()
    return render(request, 'events/home.html', {'images': images})

def schedule(request):
    posters = Schedule.objects.all()
    return render(request, 'events/schedule.html',{'posters': posters})

def results(request):
    results = Result.objects.all()
    return render(request, 'events/result_list.html', {'results': results})

def result_detail(request, result_id):
    result = get_object_or_404(Result, id=result_id)
    return render(request, 'events/result_detail.html', {'result': result})

def points_table(request):
    departments = Department.objects.all().order_by('-total_points')
    top_students_by_category = {}
    categories = Category.objects.all()

    for category in categories:
        # Get all the results for this category
        results = Result.objects.filter(category=category)

        # Create a list of students with their points in this specific category
        students_with_points = []

        for result in results:
            # Add points based on the placements in the result
            for student in result.first_place.all():
                students_with_points.append({
                    'student': student,
                    'points_in_category': 10
                })
            for student in result.second_place.all():
                students_with_points.append({
                    'student': student,
                    'points_in_category': 7
                })
            for student in result.third_place.all():
                students_with_points.append({
                    'student': student,
                    'points_in_category': 3
                })

        # Sort students by points in this category (descending order)
        students_with_points = sorted(students_with_points, key=lambda x: x['points_in_category'], reverse=True)[:5]

        # Store the students with their points in the category
        top_students_by_category[category] = students_with_points

    return render(request, 'events/points.html', {'departments': departments, 'top_students_by_category': top_students_by_category})