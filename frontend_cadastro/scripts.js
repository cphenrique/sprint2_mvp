/*
  --------------------------------------------------------------------------------------
  Função para obter a lista de carros disponíveis na API REST via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.carros.forEach(carro => insertList(carro.codigo, carro.nome))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()


/*
  --------------------------------------------------------------------------------------
  Função para colocar um projeto no servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputProjeto, inputDescricao, inputInicio, inputFim, inputCategoria, inputGerente, inputStatus) => {
  const formData = new FormData();
  formData.append('nome', inputProjeto);
  formData.append('descricao', inputDescricao);
  formData.append('inicio', inputInicio);
  formData.append('fim', inputFim);
  formData.append('id_categoria', inputCategoria);
  formData.append('id_gerente', inputGerente);
  formData.append('id_status', inputStatus);

  let url = 'http://127.0.0.1:5000/projeto';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertButton = (parent) => {
  let btn = document.createElement("button");
  let txt = document.createTextNode("del");
  btn.className = "btn btn-danger";
  btn.appendChild(txt);
  parent.appendChild(btn);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("btn-danger");
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um projeto do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/projeto?nome=' + item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo projeto
  --------------------------------------------------------------------------------------
*/
const newItem = () => {
  let inputProjeto = document.getElementById("newProjeto").value;
  let inputDescricao = document.getElementById("newDescricao").value;
  let inputInicio = document.getElementById("newInicio").value;
  let inputFim = document.getElementById("newFim").value;
  let inputCategoria = document.getElementById("newCategoria").value;
  let inputGerente = document.getElementById("newGerente").value;
  let inputStatus = document.getElementById("newStatus").value;

  if (inputProjeto === '') {
    alert("O nome do Projeto é obrigatório");
  } else {
    insertList(inputProjeto, inputDescricao, inputInicio, inputFim, inputCategoria, inputGerente, inputStatus)
    postItem(inputProjeto, inputDescricao, inputInicio, inputFim, inputCategoria, inputGerente, inputStatus)
    alert("Projeto adicionado!")
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para inserir projetos na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (nome, descricao, inicio, fim, categoria, gerente, status) => {
  var item = [nome, descricao, inicio, fim, categoria, gerente, status]
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = item[i];
  }
  insertButton(row.insertCell(-1))
  document.getElementById("newProjeto").value = "";
  document.getElementById("newDescricao").value = "";
  document.getElementById("newInicio").value = "";
  document.getElementById("newFim").value = "";
  document.getElementById("newCategoria").value = "";
  document.getElementById("newGerente").value = "";
  document.getElementById("newStatus").value = "";

  removeElement()
}

/*
  --------------------------------------------------------------------------------------
  Função para popular combobox com os dados de marca do veículo
  --------------------------------------------------------------------------------------
*/
const getListMarcas = async () => {
  let url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.forEach(marca => insertListMarcas(marca.codigo, marca.nome))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

const insertListMarcas = (codigo, marca) => {

  var combobox = document.getElementById('newMarca');
  var option = document.createElement("option");
  option.value = codigo;
  option.text = marca;
  combobox.add(option);
  combobox.selectedIndex = 0;

}

getListMarcas()

// Get references to the select elements
const marcasComboBox = document.getElementById('newMarca');
const modelosComboBox = document.getElementById('newModelo');
const anosComboBox = document.getElementById('newAno');
const valorEstimadoText = document.getElementById('newValorEstimado');

// Add an event listener to the first combo box to update the second combo box options
marcasComboBox.addEventListener('change', function() {
    const selectedOptionMarcas = marcasComboBox.value;
    
    // Clear existing options in the second combo box
    while (modelosComboBox.options.length > 0) {
      modelosComboBox.options.remove(0);
    }

    // Clear existing options in the second combo box
    while (anosComboBox.options.length > 0) {
      anosComboBox.options.remove(0);
    } 
    
    getListModelos(selectedOptionMarcas)
});


/*
  --------------------------------------------------------------------------------------
  Função para popular combobox com os modelos disponíveis por marca
  --------------------------------------------------------------------------------------
*/

const getListModelos = async (marca) => {
  let url_base = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/#/modelos';
  let url = url_base.replace('#', marca);
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.modelos.forEach(modelo => insertListModelos(modelo.codigo, modelo.nome))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

const insertListModelos = (codigo, modelo) => {

  var combobox = document.getElementById('newModelo');
  var option = document.createElement("option");
  option.value = codigo;
  option.text = modelo;
  combobox.add(option);
  combobox.selectedIndex = 0;

}

// Add an event listener to the first combo box to update the second combo box options
modelosComboBox.addEventListener('change', function() {
  const selectedOptionMarcas = marcasComboBox.value;
  const selectedOptionModelos = modelosComboBox.value;
    
    // Clear existing options in the second combo box
    while (anosComboBox.options.length > 0) {
      anosComboBox.options.remove(0);
    } 
    
    getListAnos(selectedOptionMarcas, selectedOptionModelos);
});


/*
  --------------------------------------------------------------------------------------
  Função para popular combobox com os statuses dos projetos
  --------------------------------------------------------------------------------------
*/
const getListAnos = async (marca, modelo) => {
  let url_base = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/#marca#/modelos/#modelo#/anos';
  let urla = url_base.replace('#marca#', marca);
  let urlb = urla.replace('#modelo#', modelo);
  
  fetch(urlb, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.forEach(ano => insertListAnos(ano.codigo, ano.nome))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

const insertListAnos = (codigo, ano) => {

  var combobox = document.getElementById('newAno');
  var option = document.createElement("option");
  option.value = codigo;
  option.text = ano;
  combobox.add(option);
  combobox.selectedIndex = 0;

}

// Add an event listener to the first combo box to update the second combo box options
anosComboBox.addEventListener('change', function() {
  const selectedOptionMarcas = marcasComboBox.value;
  const selectedOptionModelos = modelosComboBox.value;
  const selectedOptionAnos = anosComboBox.value;
    
    // Clear existing options in the second combo box
    valorEstimadoText.value = "";

    getValorEstimado(selectedOptionMarcas, selectedOptionModelos, selectedOptionAnos);
});


/*
  --------------------------------------------------------------------------------------
  Função para popular combobox com os statuses dos projetos
  --------------------------------------------------------------------------------------
*/
const getValorEstimado = async (marca, modelo, ano) => {
  let url_base = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/#marca#/modelos/#modelo#/anos/#ano#';
  let urla = url_base.replace('#marca#', marca);
  let urlb = urla.replace('#modelo#', modelo);
  let urlc = urlb.replace('#ano#', ano);

  fetch(urlc, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => insertValorEstimado(data.Valor))
    .catch((error) => {
      console.error('Error:', error);
    });
}

const insertValorEstimado = (valor) => {
  var textarea = document.getElementById('newValorEstimado');
  textarea.value = valor ;
  
}