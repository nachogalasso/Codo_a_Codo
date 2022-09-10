/* ToDo DATA BASE SCRIPTS - IndexedDB */

// HTML elements
const indexedDB = window.indexedDB // so then we can ask if it is created
const form = document.getElementById('form') // the input form
const tasks = document.getElementById('tasks') // the container where the tasks are gonna be display

// Asking if the indexedDB and Form are there
if(indexedDB && form) {
  let db;
  const request = indexedDB.open('taskslist', 1);
  request.onsuccess = () => {
    db = request.result;
    console.log('Open', db)
    readData()
  }

  // keyPath
  request.onupgradeneeded = (e) => {
    db = e.target.result;
    console.log('Create', db);
    const objectStore = db.createObjectStore('tasks', {keyPath: 'taskTitle' })
  }

  // Checking for errors
  request.onerror = (error) => {
    console.log('Error', error)
  }

  // FUNCTIONS TO READ, ADD, UPGRADE OR DELETE DATA. ALSO THE FORM WORK FUNCTION
  // ADD data function
  const addData = (data) => {
    const transaction = db.transaction(['tasks'], 'readwrite');
    const objectStore = transaction.objectStore('tasks');
    const request = objectStore.add(data);
    readData()
  }

  // GET DATA
  const getData = (key) => {
    const transaction = db.transaction(['tasks'], 'readwrite');
    const objectStore = transaction.objectStore('tasks');
    const request = objectStore.get(key);

    request.onsuccess = (e) => {
      form.task.value = request.result.taskTitle;
      form.priority.value = request.result.taskPriority;
      form.button.dataset.action = 'update';
      form.button.textContent = 'Update'
    }

  }

  // UPDATE DATA
  const updateData = (data) => {
    const transaction = db.transaction(['tasks'], 'readwrite');
    const objectStore = transaction.objectStore('tasks');
    const request = objectStore.put(data);

    request.onsuccess = () => {
      form.button.dataset.action = 'add';
      form.button.textContent = 'Add task';
      readData()
    }

  }

  // DELETE DATA
  const deleteData = (key) => {
    const transaction = db.transaction(['tasks'], 'readwrite');
    const objectStore = transaction.objectStore('tasks');
    const request = objectStore.delete(key);

    request.onsuccess = () => {
      readData()
    }
  }

  const readData = (data) => {
    const transaction = db.transaction(["tasks"], "readonly");
    const objectStore = transaction.objectStore("tasks");

    const fragment = document.createDocumentFragment()

    const request = objectStore.openCursor();
    
    request.onsuccess = (e) => {
      const cursor = e.target.result

      if(cursor) {
        // task
        const taskTitle = document.createElement('P');
        taskTitle.classList.add('text');
        taskTitle.textContent = cursor.value.taskTitle;
        fragment.appendChild(taskTitle);

        // priority
        const taskPriority = document.createElement('P');
        taskPriority.classList.add('text');
        taskPriority.textContent = cursor.value.taskPriority;
        fragment.appendChild(taskPriority);

        // upgdate button
        const taskUpdate = document.createElement('BUTTON');
        taskUpdate.dataset.type = 'update';
        taskUpdate.dataset.key = cursor.key
        taskUpdate.textContent = 'Update'
        taskUpdate.classList.add('green')
        fragment.appendChild(taskUpdate)

        // delete button
        const taskDelete = document.createElement('BUTTON');
        taskDelete.dataset.type = 'delete';
        taskDelete.dataset.key = cursor.key;
        taskDelete.textContent = 'Delete';
        taskDelete.classList.add('red');
        fragment.appendChild(taskDelete);

        cursor.continue()

      }else{
        tasks.textContent = '';
        tasks.appendChild(fragment)
      }
    }
  };

  // Form function
  form.addEventListener('submit', (e) => {
    e.preventDefault()
    const data = {
      taskTitle: e.target.task.value,
      taskPriority: e.target.priority.value
    }
    console.log(data)

    // button action
    if(e.target.button.dataset.action == 'add') {
      addData(data)
    }else if(e.target.button.dataset.action == 'update') {
      updateData(data)
    }

    form.reset()

  });

  // buttons from task
  tasks.addEventListener('click', (e) => {
    console.log(e.target)
    if(e.target.dataset.type == 'update') {
      getData(e.target.dataset.key);
    }else if(e.target.dataset.type == 'delete') {
      deleteData(e.target.dataset.key)
    }
  })
}

// readDATA goes outside, this is when the window opens, so it´s read whats in the data base
const readData = (data) => {
  const transaction = db.transaction(['tasks'], 'readwrite');
  const objectStore = transaction.objectStore('tasks');
  const request = objectStore.add(data)
}