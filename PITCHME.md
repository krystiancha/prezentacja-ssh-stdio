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

@[8-45](Klasa RPi)

@[50-57](Przykładowe wywołanie metody \_\_init\_\_)
@[9-24](Metoda \_\_init\_\_)
@[11-12](Przypisanie wartości polom)
@[13](Ustawienie stanu diód na wyłączone)
@[16-18](Konfiguracja GPIO)
@[20-24](Utworzenie wątków)

@[26-37](Metoda _process_input)
@[27](Wczytuj dane z stdin linia po linii)
@[28](Stwórz słownik na podstawie otrzymanej linii)
@[30-33](Jeśli otrzymano informacje na temat stanu diód, zaktualizuj go)
@[35](Jeśli otrzymano polecenie exit, to zakończ program)

@[39-45](Metoda \_output_temperature)
@[40-45](Nieskończona pętla)
@[41-45](Otwórz plik na potrzeby poniższego fragmentu kodu)
@[42-45](Odczytaj temperaturę i jeśli odczyt się powiódł, wyślij na stdout)
+++

https://www.raspberrypi.org/learning/hardware-guide/
