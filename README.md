# Dynamic Text Buffer App
![qt](https://github.com/0Swat/DynamicTextBufferApp/assets/94014791/2e2feb1d-2531-437b-9a23-33ffe526f46b)

## Opis
Dynamic Text Buffer App to aplikacja desktopowa stworzona z użyciem PyQt5, która symuluje dynamiczne zarządzanie buforem tekstu. Aplikacja używa wielowątkowości do obsługi dodawania i usuwania znaków z bufora, co umożliwia kontrolę nad prędkością tych operacji poprzez interaktywne suwaki.

## Funkcjonalności
- **Bufor tekstu**: Obszar tekstowy wyświetla aktualną zawartość bufora.
- **Pasek postępu**: Wizualizuje ilość znaków w buforze.
- **Suwaki do kontroli prędkości**:
  - Suwak do kontrolowania prędkości dodawania znaków do bufora.
  - Suwak do kontrolowania prędkości usuwania znaków z bufora.
- **Przycisk start**: Rozpoczyna działanie wątków odpowiedzialnych za dodawanie i usuwanie znaków.

## Jak uruchomić
Aby uruchomić aplikację, potrzebujesz Pythona oraz zainstalowanych bibliotek PyQt5. Możesz zainstalować wymagane zależności używając poniższego polecenia:
```bash
pip install pyqt5
