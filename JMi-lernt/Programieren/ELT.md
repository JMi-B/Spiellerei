#elt
Was ist ELT?
- Extract
	Daten herauslösen.
	- Durch Verbindung mit einer Datenquelle wie einer API oder als Rohdaten wie z. B. ein Text. 
	- Dabei ist wichtig was für Daten vorhanden sind, in welchem Format sie vorliegen, brauche ich sie alle oder nur einen Teil
- Transform
	Daten Aufbereiten
	- Was will ich wissen
	- Wie muss ich die Daten verändern, bereinigen, zusammenfassen, aufteilen oder Berechnen um die Gesuchte Aussage treffen zu können
- Load
	Daten einlesenen
		- Die Daten in ein Zeilsystem übertragen



Übernahme aus dem Script [[C:\Users\juliane.bonenkamp\Documents\data-prozess-20250714\Daten und Prozessanalyse\Woche 1\Tag 5\05 - Grundlagen von ETL.md| ELT]]

# 🧱 Grundlagen von ETL (Extract – Transform – Load)

ETL steht für **Extract (Extrahieren)**, **Transform (Transformieren)** und **Load (Laden)**. Es handelt sich um einen zentralen Prozess der Datenintegration und Datenverarbeitung – insbesondere in **Data Warehouses**, **Business Intelligence**, **Datenanalyse** und **Data Pipelines**.

---

## 🔍 1. Extract (Daten extrahieren)

### Ziel:
Daten aus einer oder mehreren **heterogenen Quellen** gewinnen.

### Typische Datenquellen:
- Relationale Datenbanken (z. B. MySQL, PostgreSQL)
- NoSQL-Datenbanken (z. B. MongoDB)
- Dateien (CSV, JSON, XML, Excel, etc.)
- APIs und Webservices (REST, SOAP)
- Logs, Sensor- oder Telemetriedaten

### Extraktionstypen:
- **Full Extraction**: Gesamtdatenbestand wird regelmäßig gezogen
- **Incremental Extraction**: Nur neue oder veränderte Daten werden extrahiert

---

## 🔧 2. Transform (Daten transformieren)

### Ziel:
Die Daten so umwandeln, dass sie für das Zielsystem geeignet und konsistent sind.

### Typische Transformationen:
- **Datenbereinigung**: Fehlerhafte, unvollständige oder doppelte Daten korrigieren
- **Datenanreicherung**: Hinzufügen externer Informationen (z. B. aus Referenztabellen)
- **Formatkonvertierung**: z. B. Zeitstempel vereinheitlichen
- **Aggregation**: Summen, Durchschnitte, Gruppierungen
- **Validierung**: Prüfen auf Geschäftsregeln, z. B. Pflichtfelder
- **Spalten/Zeilen filtern, umbenennen, neu strukturieren**

### Tools und Konzepte:
- SQL-Transformationen
- Python / Pandas, petl, PySpark
- Mapping-Tabellen
- Geschäftsregeln (Business Rules)

---

## 🗃️ 3. Load (Daten laden)

### Ziel:
Die transformierten Daten in ein **Zielsystem** integrieren.

### Zielsysteme:
- Data Warehouse (z. B. Snowflake, BigQuery, Redshift)
- Datenbanken (z. B. MariaDB, PostgreSQL)
- Data Lakes
- Dashboards / Analyse-Tools

### Ladevarianten:
- **Initial Load**: Erstbefüllung
- **Incremental Load**: Nur neue/geänderte Daten
- **Batch Load**: Zeitgesteuerte Ladevorgänge
- **Streaming Load**: Laufende Datenverarbeitung in Echtzeit

---

## 🧰 Werkzeuge (Beispiele):

| Tool           | Typ            | Bemerkung                                   |
| -------------- | -------------- | ------------------------------------------- |
| Apache NiFi    | GUI-basiert    | Visuelle Flows, gut für einfache Pipelines  |
| Talend         | GUI-basiert    | Komplexe Workflows, Business-nah            |
| petl           | Python         | Leichtgewichtig für einfache ETL-Skripte    |
| Pandas         | Python         | Datenanalyse, auch für ETL nutzbar          |
| Apache Airflow | Orchestrierung | Zeitplanung und Abfolge komplexer Pipelines |
| PySpark        | Big Data       | Für große verteilte Datenmengen             |

---

## ⚙️ Typische Anwendungsfälle:

- Zusammenführung von Kundendaten aus CRM, Webshop und Support-System
- Erstellung von Reports (z. B. Umsatz nach Region)
- Datenmigration in ein neues System
- Konsolidierung von Logfiles aus verschiedenen Servern

---

## 📌 Wichtige Herausforderungen:

- **Datenqualität**: Ungenaue oder inkonsistente Daten erschweren Analysen
- **Latenz**: Bei großen Datenmengen sind Effizienz und Performance entscheidend
- **Fehlertoleranz**: Wiederaufnahme bei Fehlern (Retry, Logging)
- **Versionierung und Historisierung**: Zeitliche Gültigkeit von Daten
- **Datenschutz**: DSGVO-konforme Verarbeitung
