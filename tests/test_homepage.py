def test_002_create_todo(home_page):
    home_page.type_new_task()
    home_page.add_new_task()
    home_page.assert_new_task()