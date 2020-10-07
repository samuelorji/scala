from structure_loader import *

STRUCTURE = load_structure()
TOPICS = STRUCTURE.topics

def test_lesson_unique():
  for topic in TOPICS:
    lessons = [lesson.id for lesson in topic.lessons]
    # it's n^2 but we won't be having more than 20 lessons in topic at this moment
    duplicates = list({lesson for lesson in lessons if lessons.count(lesson) > 1}) 
    for duplicate in duplicates:
      assert False, f"Lesson {duplicate} is duplicated in topic {topic.id}"
  
def test_prerequisites():
  lessonToCourse 
  for topic in TOPICS:
    for lesson in topic.lessons:
