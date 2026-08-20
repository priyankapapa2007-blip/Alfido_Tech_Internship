import os

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'dev-secret-key'

# In-memory data store for a simple CRUD demo
app.tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=app.tasks)


@app.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        if title:
            app.tasks.append({
                'id': len(app.tasks) + 1,
                'title': title,
                'description': description or 'No description provided.'
            })
        return redirect(url_for('index'))

    return render_template('index.html', tasks=app.tasks)


@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    for task in app.tasks:
        if task['id'] == task_id:
            app.tasks.remove(task)
            break
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)


