import random
import fake_useragent
import requests
from faker import Faker

from termcolor import colored

fake = Faker()

def generate_fake_name():
    name = fake.name()
    print(colored("Nome:", "red"), colored(name, "yellow"))
    input(colored("", "green"))

def generate_fake_cpf():
    cpf = fake.random_int(10000000000, 99999999999)
    print(colored("CPF:", "red"), colored(cpf, "yellow"))
    input(colored("", "green"))

def generate_fake_birth_date():
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%d/%m/%Y')
    print(colored("Data de Nascimento:", "red"), colored(birth_date, "yellow"))
    input(colored("", "green"))

def generate_fake_address():
    address = fake.address()
    print(colored("Endereço:", "red"), colored(address, "yellow"))
    input(colored("", "green"))

def generate_fake_cep():
    cep = fake.postcode()
    print(colored("CEP:", "red"), colored(cep, "yellow"))
    input(colored("", "green"))

def generate_fake_phone_number():
    phone_number = fake.phone_number()
    print(colored("Telefone:", "red"), colored(phone_number, "yellow"))
    input(colored("\nPressione Enter para voltar ao menu principal", "green"))

def generate_complete_data():
    generate_fake_name()
    generate_fake_cpf()
    generate_fake_birth_date()
    generate_fake_address()
    generate_fake_cep()
    generate_fake_phone_number()

def main():
    while True:
        print(colored("\n1. Gerar Nome", "blue"))
        print(colored("2. Gerar CPF", "blue"))
        print(colored("3. Gerar Data de Nascimento", "blue"))
        print(colored("4. Gerar Endereço", "blue"))
        print(colored("5. Gerar CEP", "blue"))
        print(colored("6. Gerar Número de Telefone", "blue"))
        print(colored("7. Gerar Dados Completos", "blue"))
        print(colored("8. Informações do Desenvolvedor", "blue"))
        print(colored("9. Sair", "blue"))

        choice = input(colored("Escolha uma opção: ", "green"))

        if choice == '1':
            generate_fake_name()
        elif choice == '2':
            generate_fake_cpf()
        elif choice == '3':
            generate_fake_birth_date()
        elif choice == '4':
            generate_fake_address()
        elif choice == '5':
            generate_fake_cep()
        elif choice == '6':
            generate_fake_phone_number()
        elif choice == '7':
            generate_complete_data()
        elif choice == '8':
            print(colored("Desenvolvido por 🇰 🇮 🇱 🇱 🇪 🇷 🇰 🇮 🇳 🇬 🇲 🇩 👑", "magenta"))
            input(colored("\nPressione Enter para voltar ao menu principal", "green"))
        elif choice == '9':
            print(colored("Saindo do programa...", "red"))
            break
        else:
            print(colored("Opção inválida. Tente novamente.", "red"))

if __name__ == "__main__":
    main()
