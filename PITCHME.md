# prezentacja-ssh-stdio


+++

![Logo](assets/img/controller.png)

+++

![Logo](assets/img/processing.png)

+++

```text
ssh_com_rpi_demo
├── __init__.py
├── controller
│   ├── __init__.py
│   ├── pc.py
│   └── rpi.py
├── processing
│   ├── __init__.py
│   ├── pc.py
│   └── rpi.py
└── utilities.py
```

+++

```text
ssh_com_rpi_demo
├── __init__.py
├── controller
│   ├── __init__.py
│   ├── pc.py       <---
│   └── rpi.py
├── processing
│   ├── __init__.py
│   ├── pc.py
│   └── rpi.py
└── utilities.py
```

+++?code=assets/code/ssh_com_rpi_demo/controller/rpi.py

@[1](literal_eval: str -> dict)
@[2](stdin: standardowe wejście)
@[3](Thread: wątek)

@[8](Klasa RPi)

@[50-57](Przykładowe wywołanie metody \_\_init\_\_)
@[9](Metoda \_\_init\_\_)
@[11-12](Przypisanie wartości polom)
@[14](Ustawienie stanu diód na wyłączone)
@[16-18](Konfiguracja GPIO)
@[20-30](Utworzenie wątków)

@[32](Metoda _process_input)
@[33](Wczytuj dane z stdin linia po linii)
@[34](Stwórz słownik na podstawie otrzymanej linii)
@[36-39](Jeśli otrzymano informacje na temat stanu diód, zaktualizuj go)
@[41](Jeśli otrzymano polecenie exit, to zakończ program)

@[45-51](Metoda \_output_temperature)
@[46-51](Nieskończona pętla)
@[47-51](Otwórz plik na potrzeby poniższego fragmentu kodu)
@[48-51](Odczytaj temperaturę i jeśli odczyt się powiódł, wyślij na stdout)
+++

https://www.raspberrypi.org/learning/hardware-guide/
