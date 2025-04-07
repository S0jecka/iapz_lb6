# test_task_manager.py

import task_manager

def setup_function():
    # Очистити список задач перед кожним тестом
    task_manager.tasks.clear()

def test_add_task():
    task = task_manager.add_task("Вивчити pytest")
    assert task["text"] == "Вивчити pytest"
    assert task["done"] is False
    assert len(task_manager.tasks) == 1

def test_list_tasks():
    task_manager.add_task("Задача 1")
    task_manager.add_task("Задача 2")
    tasks = task_manager.list_tasks()
    assert len(tasks) == 2
    assert tasks[0]["text"] == "Задача 1"

def test_mark_done():
    task_manager.add_task("Поставити галочку")
    result = task_manager.mark_done(0)
    assert result is True
    assert task_manager.tasks[0]["done"] is True

def test_mark_done_invalid_index():
    result = task_manager.mark_done(999)
    assert result is False

def test_delete_task():
    task_manager.add_task("Тестова задача")
    deleted = task_manager.delete_task(0)
    assert deleted["text"] == "Тестова задача"
    assert len(task_manager.tasks) == 0

def test_delete_task_invalid_index():
    deleted = task_manager.delete_task(999)
    assert deleted is None
