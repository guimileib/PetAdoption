// Dados de exemplo - simulando resposta da API
const petsData = {
    data: {
        type: "Pets",
        count: 6,
        attributes: [
            { id: 1, name: "Rex", type: "Cachorro" },
            { id: 2, name: "Mia", type: "Gato" },
            { id: 3, name: "Bob", type: "Cachorro" },
            { id: 4, name: "Luna", type: "Gato" },
            { id: 5, name: "Thor", type: "Cachorro" },
            { id: 6, name: "Nina", type: "Gato" }
        ]
    }
};

const peopleData = [
    { id: 1, first_name: "João", last_name: "Silva", pet_name: "Rex", pet_type: "Cachorro" },
    { id: 2, first_name: "Maria", last_name: "Santos", pet_name: "Mia", pet_type: "Gato" },
    { id: 3, first_name: "Pedro", last_name: "Oliveira", pet_name: "Bob", pet_type: "Cachorro" }
];

function renderPetCards() {
    const petsList = document.getElementById('petsList');
    petsList.innerHTML = '';

    petsData.data.attributes.forEach(pet => {
        const petCard = document.createElement('div');
        petCard.className = 'card';
        petCard.innerHTML = `
            <div class="card-img">${pet.type === 'Cachorro' ? '🐶' : '🐱'}</div>
            <div class="card-body">
                <h3 class="card-title">${pet.name}</h3>
                <p class="card-text">Tipo: ${pet.type}</p>
            </div>
            <div class="card-footer">
                <a href="#adoption" class="btn btn-secondary" onclick="selectPet(${pet.id})">Adotar</a>
            </div>
        `;
        petsList.appendChild(petCard);
    });
}

function renderPetOptions() {
    const petSelect = document.getElementById('pet_id');
    petSelect.innerHTML = '<option value="">Selecione um pet</option>';

    petsData.data.attributes.forEach(pet => {
        const option = document.createElement('option');
        option.value = pet.id;
        option.textContent = `${pet.name} (${pet.type})`;
        petSelect.appendChild(option);
    });
}

function renderPeopleTable() {
    const peopleList = document.getElementById('peopleList');
    peopleList.innerHTML = '';

    peopleData.forEach(person => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${person.id}</td>
            <td>${person.first_name}</td>
            <td>${person.last_name}</td>
            <td>${person.pet_name}</td>
            <td>${person.pet_type}</td>
            <td>
                <div class="action-buttons">
                    <button class="btn btn-sm btn-primary" onclick="viewPerson(${person.id})">Ver</button>
                </div>
            </td>
        `;
        peopleList.appendChild(row);
    });
}

function renderPetsTable() {
    const petsTable = document.getElementById('petsTable');
    petsTable.innerHTML = '';

    petsData.data.attributes.forEach(pet => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${pet.id}</td>
            <td>${pet.name}</td>
            <td>${pet.type}</td>
            <td>
                <div class="action-buttons">
                    <button class="btn btn-sm btn-danger" onclick="deletePet(${pet.id}, '${pet.name}')">Excluir</button>
                </div>
            </td>
        `;
        petsTable.appendChild(row);
    });
}

function selectPet(petId) {
    document.getElementById('pet_id').value = petId;
}

function viewPerson(personId) {
    const person = peopleData.find(p => p.id === personId);
    if (person) {
        alert(`Detalhes do Adotante:\nNome: ${person.first_name} ${person.last_name}\nPet: ${person.pet_name} (${person.pet_type})`);
    }
}

function deletePet(petId, petName) {
    if (confirm(`Tem certeza que deseja excluir o pet "${petName}"?`)) {
        const index = petsData.data.attributes.findIndex(pet => pet.id === petId);
        if (index !== -1) {
            petsData.data.attributes.splice(index, 1);
            petsData.data.count--;
            renderPetCards();
            renderPetOptions();
            renderPetsTable();
            alert(`Pet "${petName}" excluído com sucesso!`);
        }
    }
}

// Gerenciamento de abas
document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', () => {
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        
        tab.classList.add('active');
        const tabName = tab.getAttribute('data-tab');
        document.getElementById(`${tabName}-tab`).classList.add('active');
    });
});

document.getElementById('adoptionForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = {
        first_name: document.getElementById('first_name').value,
        last_name: document.getElementById('last_name').value,
        age: parseInt(document.getElementById('age').value),
        pet_id: parseInt(document.getElementById('pet_id').value)
    };
    
    const nameRegex = /^[a-zA-Z]+$/;
    if (!nameRegex.test(formData.first_name) || !nameRegex.test(formData.last_name)) {
        alert('Nome e sobrenome devem conter apenas letras.');
        return;
    }
    
    console.log('Dados do formulário:', formData);
    
    const petInfo = petsData.data.attributes.find(pet => pet.id === formData.pet_id);
    
    const newPerson = {
        id: peopleData.length + 1,
        first_name: formData.first_name,
        last_name: formData.last_name,
        pet_name: petInfo.name,
        pet_type: petInfo.type
    };
    
    peopleData.push(newPerson);
    renderPeopleTable();
    
    document.getElementById('adoptionForm').reset();
    
    alert('Solicitação de adoção enviada com sucesso!');
});

document.addEventListener('DOMContentLoaded', () => {
    renderPetCards();
    renderPetOptions();
    renderPeopleTable();
    renderPetsTable();
});