import unittest

import app


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.app.test_client()
        app.app.tasks.clear()

    def test_home_page_renders(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Flask Fundamentals Demo', response.data)

    def test_can_create_task(self):
        response = self.client.post('/tasks', data={
            'title': 'Write README',
            'description': 'Document the demo app',
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Write README', response.data)

    def test_can_delete_task(self):
        app.app.tasks.append({'id': 1, 'title': 'Delete me', 'description': 'Temporary task'})
        response = self.client.post('/tasks/1/delete', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Delete me', response.data)


if __name__ == '__main__':
    unittest.main()
