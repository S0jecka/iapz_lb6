



import MyProject

def setup_function():
    # Очистити список задач перед кожним тестом
    MyProject.tasks.clear()

def test_add_task():
    task = MyProject.add_task("Вивчити pytest")
    assert task["text"] == "Вивчити pytest"
    assert task["done"] is False
    assert len(MyProject.tasks) == 1

def test_list_tasks():
    MyProject.add_task("Задача 1")
    MyProject.add_task("Задача 2")
    tasks = MyProject.list_tasks()
    assert len(tasks) == 2
    assert tasks[0]["text"] == "Задача 1"

def test_mark_done():
    MyProject.add_task("Поставити галочку")
    result = MyProject.mark_done(0)
    assert result is True
    assert MyProject.tasks[0]["done"] is True

def test_mark_done_invalid_index():
    result = MyProject.mark_done(999)
    assert result is False

def test_delete_task():
    MyProject.add_task("Тестова задача")
    deleted = MyProject.delete_task(0)
    assert deleted["text"] == "Тестова задача"
    assert len(MyProject.tasks) == 0

def test_delete_task_invalid_index():
    deleted = MyProject.delete_task(999)
    assert deleted is None
