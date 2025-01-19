import streamlit as st

# Initialize the session state if it doesn't exist
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []

# Title of the application
st.title('To-Do List App')

# Function to add a task to the list
def add_task(task):
    st.session_state.todo_list.append({'task': task, 'completed': False})

# Function to remove a task from the list
def remove_task(index):
    st.session_state.todo_list.pop(index)

# Function to toggle the completion status of a task
def toggle_task(index):
    st.session_state.todo_list[index]['completed'] = not st.session_state.todo_list[index]['completed']

# Text input for new task
new_task = st.text_input('Enter a task', '')

# Button to add the new task
if st.button('Add Task'):
    if new_task:
        add_task(new_task)
        new_task = ''  # Clear the input box after adding

# Display tasks with options to delete or mark them as completed
for i, item in enumerate(st.session_state.todo_list):
    col1, col2, col3 = st.columns([0.8, 0.1, 0.1])
    # Using checkbox to mark the task as completed or not
    completed = col1.checkbox(item['task'], item['completed'], key=str(i))
    if completed != item['completed']:
        toggle_task(i)
    
    # Button to delete the task
    if col2.button('Delete', key=f'Del_{i}'):
        remove_task(i)

    # An optional button to toggle completion without the checkbox
    if col3.button('Done' if not item['completed'] else 'Undo', key=f'Toggle_{i}'):
        toggle_task(i)

# Optional: Run your app
# To run the app, save this script and run the following command in your terminal:
# streamlit run todo_app.py
