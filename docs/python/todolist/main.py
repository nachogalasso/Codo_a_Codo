# from pyodide import creat_proxy
# print("Hello World!!")
# Here we create the functionallity of our ToDo List

# First we need to gather our input and its value
# we create a List to gather all the tasks
tasks = []

# Get elements. We need to use the "id" from the input
todo_input = Element("task-input")
error_message = Element("error")
# here we fetch our list elements. 1st the container and then the inner element
taskList = Element("item").select(".list_item", from_content=True)
# now we need the element to append the tasks and that is our ul
list = Element("items")


# js.console.log(todo_input.element) this is how we get access to the input element
def add_todo(*args):
   # js.console.log('button-clicked')
   input_value = todo_input.element.value
   # js.console.log(input_value)
   # we check if the value is not blank
   if input_value:
      error_message.element.textContent = ""
      # js.console.log(input_value)
      # js.console.log(taskList.element)
      # Now is time to create an object with our task, but first we need to add an id for each task. we use 
      # format "f" to make the id an interger number, before => todo_id = "todo_"+str(len(tasks))
      todo_id = f"todo_{len(tasks)}"
      # now the object =>
      todo = {
         "id": todo_id,
         "text": input_value,
         "done": False
      }
      # now we append the object to our tasks list
      tasks.append(todo)
      # to create a new task we need to clone the node. We need to use two arguments, the id and our
      # list
      task = taskList.clone(todo_id, to=list)
      task_content = task.select("p")
      task_content.element.textContent = input_value
      task_checkbox = task.select("input")
      task_checkbox.element.checked = False
      # now we append all the elements to our list. Don´t forget the element and to appendChild
      list.element.appendChild(task.element)
      # to put the input in blank
      todo_input.clear()
      
      # function for the checkbox to remove the id
      def complete_task(task_id):
         task_checkbox_element = task_checkbox.element
         task_checkbox_element.checked = True
         task_checkbox_element.disabled = True
         task_content.element.style.textDecoration = "line-through"
         task_content.element.style.color = "red"
         
      task_checkbox.element.onclick = complete_task
      
   else:
      error_message.element.textContent = "Please insert a Task"   
   # is important that if we are gonna use the py-onClick="function()" we need to add an 'id' to the button
   
"""
an other way to use the button, we can use an addEventListener which we can use with 'pyodide'
addButton = document.getElementById('submit')

def add_todo(e):
   js.console.log('Button clicked')

event = creat_proxy(add_todo)
addButton.addEventListener("click", event)
"""