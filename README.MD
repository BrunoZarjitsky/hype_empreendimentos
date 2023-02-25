# Business Case Hype Empreendimentos
### **Bruno Zarjitsky - Desenvolvedor Backend**
### **brunozar@poli.ufrj.br**
### **[LinkedIn](https://www.linkedin.com/in/brunozar "linkedin.com/in/brunozar")**
### **[GitHub](https://github.com/BrunoZarjitsky)**
---
### **Objetivo:** Desenvolver uma API para simular o output de um equipamento chamado HBM+ (Heart Beat Monitor Plus), que serve para realizar análises de padrão de sinais de batimentos cardiácos de pacientes.


Para simular o output do equipamento, será utlizado a seguinte equação:
Y = -0.06366 + 0.12613 * cos(\pi*x/500) + 0.12258 * cos(\pi*x/250) + 0.01593 * sin(\pi*x/500) + 0.03147 * sin(\pi*x/250)$$
Onde x é o tempo em milissegundos.

---

Para implementar essa API optei por utilizar a linguagem **Python** e o framework **Django**. Escolhi essas tecnologias principalmente pois na introdução do desafio foi citado que futuramente essa API seria utilizada para fazer analises e predições para pacientes, e acredito que as ferramentas que o Django apresenta para manusear bancos de dados atenderão muito bem esses objetivos.

## **Requisitos do sistema**
 - Python 3.10 (sudo apt-get install python3.10 )
 - venv (sudo apt-get install python3-venv)

## **Como rodar o projeto**
Criando o ambiente virtual:

    python -m virtualenv venv

Ativando o ambiente virtual:

    source venv/bin/activate

Instalando os requisitos da aplicação

    pip install -r requirements.txt

Iniciando o servidor

    ./manage.py runserver

## Lista de endpoints
 - localhost:8000/HBM_plus/read_heart_beat_monitor/ -> Realiza uma leitura no HBM+
 - localhost:8000/stress_test/run_stress_test/ -> Faz um teste de estresse no endpoint

## Detalhamento dos endpoints
### /HBM_plus/read_heart_beat_monitor/

Utiliza o tempo em milissegundos para calcular o output utilizando a equação já mencionada. esse endpoint não espera argumentos de entrada, e seu retorno é no formato
```JSON
{ "value": "valor_calculado" }
```

### /stress_test/run_stress_test/

Esse endpoint usa um script para fazer requisições ao endpoint /HBM_plus/read_heart_beat_monitor/, com objetivo de calcular quantas requisições por segundo a API consegue executar. Para isso, recebe time_testing_in_seconds como argumento, essa variável define o tempo que o teste de estresse vai ficar sendo execudato, caso o argumento não seja encontrado no body, é utilizado 1 segundo como padrão, e retorna quantas iterações foram executadas.
```JSON
{
    "requests": "requests_executadas",
    "requests_per_seconds": "media_requests_executadas",
    "time_in_seconds": "tempo_de_execução"
}
```
