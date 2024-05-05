### 1. Introduction

#### a. Programos Apžvalga
Šio darbo tikslas yra sukurti Python programą, skirtą valdyti produktų katalogą ir pirkinių sąrašus. Programa pritaiko nuoliadas ir apskaičiuoja sumą. Programoje naudojamas objektinis programavimas, 
dizaino šablonai, failų įvedimą/išvedimą.

#### b. Kaip Paleisti Programą
Norėdami paleisti programą:
1. Atsisiųskite pateiktą Python skriptą.
2. Padėkite skriptą į katalogą kartu su įvesties failais (`Produktai.txt` ir `Pirkiniai.txt`).
3. Atidarykite terminalą ar komandinę eilutę.
4. Naviguokite į katalogą, kuriame yra skriptas ir įvesties failai.
5. Paleiskite skriptą naudodami komandą `python script_name.py`.

#### c. Kaip Naudoti Programą
1. Programa įkelia produktų informaciją iš `Produktai.txt` ir pirkinių sąrašo elementus iš `Pirkiniai.txt`.
2. Ji atnaujina produktų kiekius kataloge pagal pirkinių sąrašą.
3. Galiausiai ji skaičiuoja viso pirkinių sąraše esančių elementų sumą, atsižvelgdama į taikomus nuolaidas, jei jos yra taikomos, ir išsaugo sumą į failą `Suma.txt`.

### 2. Body/Analysis

#### a. Produktų Klasė
```python
class Product:
    def __init__(self, name, quantity, price, discount):
        self._name = name
        self._quantity = quantity
        self._price = price
        self._discount = discount

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def price(self):
        return self._price

    @property
    def discount(self):
        return self._discount
```
Paaiškinimas:
- Ši klasė atstovauja produktui su atributais, tokiu kaip pavadinimas, kiekis, kaina ir nuolaida.
- Getter ir setter metodai užtikrina duomenų uždarbį ir suteikia sąsają norint pasiekti ir modifikuoti atributus.

#### b. Produktų Kūrėjo Klasė
```python
class ProductFactory:
    @staticmethod
    def create_product(name, quantity, price, discount):
        return Product(name, quantity, price, discount)
```
Paaiškinimas:
- `ProductFactory` klasė įgyvendina Factory dizaino šabloną, kad paslėptų `Product` instancijų kūrimą.
- `create_product` metodas sukuria ir grąžina naują `Product` instanciją su nurodytais atributais, skatinant silpnąjį ryšį.

#### c. Produktų Katalogo Klasė
```python
class ProductCatalog:
    _instance = None

    def __init__(self):
        self._products = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

  
```
Paaiškinimas:
- `ProductCatalog` valdo produktus ir įgyvendina Singleton dizaino šabloną, užtikrinantį vieną instanciją visoje programoje.
- Metodai, tokie kaip `add_product`, `find_product`, `update_product`, `load_products_from_file` ir `save_products_to_file`, palengvina produktų valdymo operacijas.

#### d. Pirkinių Sąrašo Klasė
```python
class ShoppingList:
    def __init__(self):
        self._items = {}

    # Metodai elementams įkelti iš failo, gauti elementus, atnaujinti kiekius...
```
Paaiškinimas:
- `ShoppingList` palaiko pirkinių sąrašą.
- Metodai, tokie kaip `load_items_from_file`, `get_items` ir `update_quantity`, padeda operacijoms, susijusioms su elementų įkėlimu, gavimu ir atnaujinimu.

#### e. Integracija ir Darbo Eiga (Pagrindinė Funkcija)
```python
def main():
    product_catalog = ProductCatalog.get_instance()
    product_catalog.load_products_from_file('Produktai.txt')

    shopping_list = ShoppingList()
    shopping_list.load_items_from_file('Pirkiniai.txt')

    products_to_update = shopping_list.get_items()

    product_catalog.update_product_quantities(products_to_update)
    product_catalog.save_products_to_file('Produktai.txt')

    total_amount = product_catalog.calculate_total(products_to_update)

    with open("Suma.txt", "w") as file:
        file.write(f"Bendra suma: {total_amount:.2f} EUR\n")


if __name__ == "__main__":
    main()
```
Paaiškinimas:
- `main` funkcija koordinuoja `ProductCatalog` ir `ShoppingList` klasių integraciją.
- Ji įkelia produktų informaciją ir pirkinių sąrašo elementus, atnaujina produktų kiekius, skaičiuoja visos sumos, ir išsaugo rezultatą į failą.

### 3. Rezultatai ir Išvados

#### a. Darbo Rezultatai (Programa)
Programa efektyviai valdo produktų katalogus ir pirkinių sąrašus, atnaujina kiekius, skaičiuoja visų sumas.

#### b. Išvados
Ši programa sėkmingai veikia. Galimos tolesnės perspektyvos apima vartotojo sąsajų tobulinimą, integravimą su išorinėmis duomenų bazėmis ir papildomų funkcijų pridėjimą.

#### c. Galimos Perspektyvos
Galimos tobulinimo galimybės apima vartotojo sąsajų pridėjimą, integravimą su duomenų bazėmis. 
