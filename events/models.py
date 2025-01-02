from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

class Department(models.Model):
    name = models.CharField(max_length=100)
    total_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    individual_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Result(models.Model):
    program = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    first_place = models.ManyToManyField(Student, related_name='first_place', blank=True)
    second_place = models.ManyToManyField(Student, related_name='second_place', blank=True)
    third_place = models.ManyToManyField(Student, related_name='third_place', blank=True)

    def __str__(self):
        return f"{self.program} - Results"


@receiver(m2m_changed, sender=Result.first_place.through)
def update_first_place_points(sender, instance, action, reverse, pk_set, **kwargs):
    if action in ["post_add", "post_remove"]:
        points = 10
        adjust_points(instance, pk_set, points, reverse)


@receiver(m2m_changed, sender=Result.second_place.through)
def update_second_place_points(sender, instance, action, reverse, pk_set, **kwargs):
    if action in ["post_add", "post_remove"]:
        points = 7
        adjust_points(instance, pk_set, points, reverse)


@receiver(m2m_changed, sender=Result.third_place.through)
def update_third_place_points(sender, instance, action, reverse, pk_set, **kwargs):
    if action in ["post_add", "post_remove"]:
        points = 3
        adjust_points(instance, pk_set, points, reverse)


def adjust_points(result_instance, student_ids, points, reverse):
    """Adjust points for students and their departments."""
    for student_id in student_ids:
        try:
            student = Student.objects.get(id=student_id)
            department = student.department

            if reverse:  # Removing points
                student.individual_score -= points
                department.total_points -= points
            else:  # Adding points
                student.individual_score += points
                department.total_points += points

            student.save()
            department.save()
        except Student.DoesNotExist:
            pass

            

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.title} - Image"
    
class Schedule(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Posters/')

    def __str__(self):
        return f"{self.title} - Schedule"