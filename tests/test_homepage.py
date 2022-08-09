def test_002_create_todo(home_page):
    home_page.type_new_task()
    home_page.add_new_task()
    home_page.assert_new_task()


def test_006_complete_todo(home_page):
    home_page.mark_task_done()
    home_page.verify_absence_done()
    home_page.assert_absence_done()


def test_008_uncomplete_todo(home_page):
    home_page.mark_task_undone()
    home_page.mark_task_undone()
    home_page.verify_absence_undone()
    home_page.assert_absence_undone()


def test_004_destroy_todo(home_page):
    home_page.delete_task()
    home_page.delete_task()
    home_page.delete_task()
    home_page.assert_absence_task()

