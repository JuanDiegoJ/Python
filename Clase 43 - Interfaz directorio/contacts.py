import csv

#Creación del método contacto
class Contact:
    #Constructor
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

#Clase que almacena la lista de contactos
class ContactBook:
    def __init__(self):
        self._contacts = []
    #Método que añade un contacto
    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()
    #método que muestra la lista de contactos
    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
    #Organiza el contacto
    def _print_contact(self, contact):
        print('---*---*---*-a--*---*---*---*')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('---*---*---*---*---*---*---*')
    #Borra el contacto
    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
    #Busca un contacto
    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()
    def _not_found(self):
        print('Contacto no encontrado')
    #Actualiza el contacto
    def update_contact(self, name, n_name, n_phone, n_email):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                contact.name = n_name
                contact.phone = n_phone
                contact.email = n_email
                print('Contacto actualizado')
                self._save()
    def validate_contact(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                return True
            else:
                return False
    #Guarda el contacto en un archivo CSV
    def _save(self):
        with open('contacts.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))
            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))
def run():
    #Instancia de la clase
    contact_book = ContactBook()
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            contact_book.add(row[0], row[1], row[2])
    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el teléfono del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            name = str(input('Cuál es el nombre del contacto: '))
            if contact_book.validate_contact(name) == True:
                n_name = str(input('Ingrese el nuevo nombre: '))
                phone = str(input('Ingrese el nuevo teléfono: '))
                email = str(input('Ingrese el nuevo apellido: '))
                contact_book.update_contact(name, n_name, phone, email)
            else:
                print('Contacto no encontrado')

            

        elif command == 'b':
            name = str(input('Cuál es el nombre del contacto: '))
            contact_book.search(name)
            
        elif command == 'e':
            name = str(input('Cuál es el nombre del contacto: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')

if __name__ == '__main__':
    run()