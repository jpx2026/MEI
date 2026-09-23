const form = document.querySelector('#task-form');
const input = document.querySelector('#task-input');
const taskList = document.querySelector('#task-list');
const emptyMessage = document.querySelector('#empty-message');

function updateEmptyMessage() {
	emptyMessage.hidden = taskList.children.length > 0;
}

function createTask(taskText) {
	const item = document.createElement('li');
	item.className = 'task-item';

	const checkbox = document.createElement('input');
	checkbox.type = 'checkbox';
	checkbox.setAttribute('aria-label', `Concluir: ${taskText}`);

	const text = document.createElement('span');
	text.textContent = taskText;

	const deleteButton = document.createElement('button');
	deleteButton.className = 'delete-button';
	deleteButton.type = 'button';
	deleteButton.textContent = 'Apagar';

	checkbox.addEventListener('change', () => {
		item.classList.toggle('completed', checkbox.checked);
	});

	deleteButton.addEventListener('click', () => {
		item.remove();
		updateEmptyMessage();
	});

	item.append(checkbox, text, deleteButton);
	return item;
}

form.addEventListener('submit', (event) => {
	event.preventDefault();

	const taskText = input.value.trim();
	if (!taskText) {
		return;
	}

	taskList.append(createTask(taskText));
	input.value = '';
	input.focus();
	updateEmptyMessage();
});

updateEmptyMessage();
