from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    shortdescription = models.CharField(max_length=255)
    image_src = models.CharField(max_length=510, default='N/A')

    def __str__(self):
        return self.course_name

class Section(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    section_name = models.CharField(max_length=255)

    def __str__(self):
        return self.section_name

class Quiz(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=255)

    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    isCorrect = models.BooleanField()
    answer_text = models.CharField(max_length=255)

class Video_Module(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=255)
    video_link = models.CharField(max_length=255)
    video_description = models.CharField(max_length=255)
class Link(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    link_title = models.CharField(max_length=255)
    link_src = models.CharField(max_length=1500)


